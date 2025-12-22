#!/usr/bin/env python3
"""extract_transcript.py

Rebuild `transcript.json` from iMessage screenshot images.

Approach (robust for iOS Messages screenshots):
- Detect message bubbles by color/shape (green = User/right, gray = Dealer/left)
- OCR each bubble crop individually
- OCR centered timestamp lines and map each bubble to the nearest timestamp above it
- Convert relative timestamps (Today/Yesterday/weekday-only) to absolute dates using screenshot file date

Output: `transcript.json` in the same directory as this script.
"""

from __future__ import annotations

import json
import os
import re
import shutil
from dataclasses import dataclass
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Tuple

import cv2
import numpy as np
import pytesseract
from exifread import process_file


# Configure tesseract path (macOS/Homebrew friendly)
_tesseract_path = shutil.which("tesseract")
if _tesseract_path:
    pytesseract.pytesseract.tesseract_cmd = _tesseract_path


@dataclass(frozen=True)
class TimestampLine:
    y_center: int
    raw_text: str


@dataclass(frozen=True)
class Bubble:
    x: int
    y: int
    w: int
    h: int
    sender: str  # "User" or "Dealer"

    @property
    def top(self) -> int:
        return self.y

    @property
    def bottom(self) -> int:
        return self.y + self.h


WEEKDAY_TO_INT = {
    "monday": 0,
    "tuesday": 1,
    "wednesday": 2,
    "thursday": 3,
    "friday": 4,
    "saturday": 5,
    "sunday": 6,
}

MONTH_TO_INT = {
    "jan": 1,
    "feb": 2,
    "mar": 3,
    "apr": 4,
    "may": 5,
    "jun": 6,
    "jul": 7,
    "aug": 8,
    "sep": 9,
    "sept": 9,
    "oct": 10,
    "nov": 11,
    "dec": 12,
}


def _safe_int(x: str, default: int = 0) -> int:
    try:
        return int(x)
    except Exception:
        return default


def get_screenshot_datetime(image_path: str) -> datetime:
    """Best-effort: EXIF DateTimeOriginal, else file mtime."""
    try:
        with open(image_path, "rb") as f:
            tags = process_file(f, details=False)
        if "EXIF DateTimeOriginal" in tags:
            return datetime.strptime(str(tags["EXIF DateTimeOriginal"]), "%Y:%m:%d %H:%M:%S")
        if "Image DateTime" in tags:
            return datetime.strptime(str(tags["Image DateTime"]), "%Y:%m:%d %H:%M:%S")
    except Exception:
        pass

    mtime = os.path.getmtime(image_path)
    return datetime.fromtimestamp(mtime)


def _parse_time(hh: str, mm: str, ampm: str) -> Tuple[int, int]:
    hour = _safe_int(hh)
    minute = _safe_int(mm)
    ampm = ampm.strip().upper()
    if ampm == "PM" and hour != 12:
        hour += 12
    if ampm == "AM" and hour == 12:
        hour = 0
    return hour, minute


def _closest_past_weekday(base_date: datetime, weekday_int: int) -> datetime:
    """Return date (no time change) for the closest past occurrence of weekday, including same day."""
    delta = (base_date.weekday() - weekday_int) % 7
    return base_date - timedelta(days=delta)


def parse_timestamp_text(raw: str, screenshot_dt: datetime) -> Optional[datetime]:
    """Parse iMessage timestamp line into an absolute datetime."""
    s = raw.strip()
    s = re.sub(r"\s+", " ", s)

    # Common OCR oddities: missing space before AM/PM
    s = re.sub(r"(\d{1,2}:\d{2})(AM|PM)\b", r"\1 \2", s, flags=re.IGNORECASE)

    # Today/Yesterday
    m = re.search(r"\b(Today|Yesterday)\s+(\d{1,2}):(\d{2})\s*(AM|PM)\b", s, flags=re.IGNORECASE)
    if m:
        which = m.group(1).lower()
        hour, minute = _parse_time(m.group(2), m.group(3), m.group(4))
        base = screenshot_dt.replace(hour=0, minute=0, second=0, microsecond=0)
        if which == "yesterday":
            base = base - timedelta(days=1)
        return base.replace(hour=hour, minute=minute)

    # Weekday-only: "Thursday 10:13 PM" etc.
    m = re.search(r"\b(Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday)\s+(\d{1,2}):(\d{2})\s*(AM|PM)\b", s, flags=re.IGNORECASE)
    if m:
        wd = WEEKDAY_TO_INT[m.group(1).lower()]
        hour, minute = _parse_time(m.group(2), m.group(3), m.group(4))
        base = screenshot_dt.replace(hour=0, minute=0, second=0, microsecond=0)
        day = _closest_past_weekday(base, wd)
        return day.replace(hour=hour, minute=minute)

    # Absolute (most common): "Oct 9, 2024 at 4:32 PM"
    m = re.search(
        r"\b([A-Za-z]{3,4})\s+(\d{1,2}),\s*(\d{4})\s*(?:at\s+)?(\d{1,2}):(\d{2})\s*(AM|PM)\b",
        s,
        flags=re.IGNORECASE,
    )
    if m:
        mon = MONTH_TO_INT.get(m.group(1).lower()[:3])
        if not mon:
            return None
        day = _safe_int(m.group(2))
        year = _safe_int(m.group(3))
        hour, minute = _parse_time(m.group(4), m.group(5), m.group(6))
        return datetime(year, mon, day, hour, minute)

    # With leading weekday and no year: "Mon, Jan 27 at 1:57 PM" or "Mon, Jan 27, 1:57 PM"
    m = re.search(
        r"\b(?:Mon|Tue|Wed|Thu|Fri|Sat|Sun),?\s+([A-Za-z]{3})\s+(\d{1,2})\s*(?:at\s+|,\s*)?(\d{1,2}):(\d{2})\s*(AM|PM)\b",
        s,
        flags=re.IGNORECASE,
    )
    if m:
        mon = MONTH_TO_INT.get(m.group(1).lower()[:3])
        if not mon:
            return None
        day = _safe_int(m.group(2))
        hour, minute = _parse_time(m.group(3), m.group(4), m.group(5))

        # Choose a plausible year based on screenshot date
        year = screenshot_dt.year
        candidate = datetime(year, mon, day, hour, minute)
        # If candidate is >30 days in the future vs screenshot, assume previous year.
        if candidate - screenshot_dt > timedelta(days=30):
            candidate = datetime(year - 1, mon, day, hour, minute)
        return candidate

    return None


def format_timestamp(dt: datetime, approx: bool) -> str:
    ts = dt.strftime("%a, %b %d, %Y, %I:%M %p")
    return f"{ts} (approx)" if approx else ts


def preprocess_for_ocr(img_bgr: np.ndarray) -> np.ndarray:
    gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
    thr = cv2.adaptiveThreshold(
        gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 9
    )
    return thr


def preprocess_bubble_for_ocr(img_bgr: np.ndarray, sender: str) -> np.ndarray:
    """
    Bubble-aware preprocessing.
    - Dealer (gray): dark text on light background -> adaptive threshold
    - User (green): light text on dark/colored background -> isolate near-white text then invert
    """
    # Upscale for better OCR
    scale = 2.0
    img_bgr = cv2.resize(img_bgr, None, fx=scale, fy=scale, interpolation=cv2.INTER_CUBIC)

    if sender != "User":
        return preprocess_for_ocr(img_bgr)

    hsv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)
    # White-ish text: low saturation, high value
    white = cv2.inRange(hsv, (0, 0, 210), (180, 70, 255))
    white = cv2.medianBlur(white, 3)
    # Make text black on white background
    inv = 255 - white
    return inv


def extract_timestamp_lines(img_bgr: np.ndarray) -> List[TimestampLine]:
    """OCR the screen and return candidate timestamp lines with y positions."""
    proc = preprocess_for_ocr(img_bgr)

    data = pytesseract.image_to_data(
        proc, output_type=pytesseract.Output.DICT, config="--oem 3 --psm 6"
    )

    # Group words by (block, par, line)
    lines: Dict[Tuple[int, int, int], List[int]] = {}
    n = len(data.get("text", []))
    for i in range(n):
        txt = (data["text"][i] or "").strip()
        if not txt:
            continue
        key = (data["block_num"][i], data["par_num"][i], data["line_num"][i])
        lines.setdefault(key, []).append(i)

    candidates: List[TimestampLine] = []

    ts_hint = re.compile(
        r"\b(?:Today|Yesterday|Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday|"
        r"Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec)\b",
        re.IGNORECASE,
    )

    for idxs in lines.values():
        words = []
        ys, ye = [], []
        for i in idxs:
            t = (data["text"][i] or "").strip()
            if not t:
                continue
            # ignore some UI words that frequently appear around the header
            if t.lower() in {"text", "message", "sms"}:
                continue

            words.append(t)
            y = data["top"][i]
            h = data["height"][i]
            ys.append(y)
            ye.append(y + h)

        if not words:
            continue

        line_text = " ".join(words)
        line_text = re.sub(r"\s+", " ", line_text).strip()
        if not line_text:
            continue

        if not ts_hint.search(line_text):
            continue

        y_center = int((min(ys) + max(ye)) / 2)
        candidates.append(TimestampLine(y_center=y_center, raw_text=line_text))

    candidates.sort(key=lambda t: t.y_center)

    # de-dupe identical strings
    out: List[TimestampLine] = []
    seen = set()
    for c in candidates:
        if c.raw_text in seen:
            continue
        seen.add(c.raw_text)
        out.append(c)

    return out


def _mask_cleanup(mask: np.ndarray, kernel: int = 17) -> np.ndarray:
    k = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (kernel, kernel))
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, k, iterations=2)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, k, iterations=1)
    return mask


def find_bubbles(img_bgr: np.ndarray) -> List[Bubble]:
    """Detect bubble bounding boxes using color masks + contour filtering."""
    h, w = img_bgr.shape[:2]
    hsv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)

    green_mask = cv2.inRange(hsv, (35, 40, 60), (95, 255, 255))
    gray_mask = cv2.inRange(hsv, (0, 0, 170), (180, 60, 245))

    # Remove header/top and composer/bottom areas
    top_cut = int(h * 0.12)
    bottom_cut = int(h * 0.12)
    green_mask[:top_cut, :] = 0
    gray_mask[:top_cut, :] = 0
    green_mask[h - bottom_cut :, :] = 0
    gray_mask[h - bottom_cut :, :] = 0

    green_mask = _mask_cleanup(green_mask, kernel=19)
    gray_mask = _mask_cleanup(gray_mask, kernel=19)

    bubbles: List[Bubble] = []

    def _contours_to_bubbles(mask: np.ndarray) -> None:
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for c in contours:
            x, y, bw, bh = cv2.boundingRect(c)
            area = bw * bh

            if area < 3500:
                continue
            if bw < int(w * 0.20):
                continue
            if bh < int(h * 0.03):
                continue
            if bw > int(w * 0.98) and bh > int(h * 0.25):
                continue

            cx = x + bw / 2
            sender = "User" if cx > w * 0.55 else "Dealer"
            bubbles.append(Bubble(x=x, y=y, w=bw, h=bh, sender=sender))

    _contours_to_bubbles(green_mask)
    _contours_to_bubbles(gray_mask)

    # De-dupe overlapping boxes (keep larger)
    bubbles.sort(key=lambda b: (b.y, b.x))
    pruned: List[Bubble] = []

    def iou(a: Bubble, b: Bubble) -> float:
        ax1, ay1, ax2, ay2 = a.x, a.y, a.x + a.w, a.y + a.h
        bx1, by1, bx2, by2 = b.x, b.y, b.x + b.w, b.y + b.h
        ix1, iy1 = max(ax1, bx1), max(ay1, by1)
        ix2, iy2 = min(ax2, bx2), min(ay2, by2)
        iw, ih = max(0, ix2 - ix1), max(0, iy2 - iy1)
        inter = iw * ih
        if inter <= 0:
            return 0.0
        union = (a.w * a.h) + (b.w * b.h) - inter
        return inter / union if union else 0.0

    for b in bubbles:
        merged = False
        for k, kept in enumerate(pruned):
            if iou(b, kept) > 0.55:
                if b.w * b.h > kept.w * kept.h:
                    pruned[k] = b
                merged = True
                break
        if not merged:
            pruned.append(b)

    pruned.sort(key=lambda b: (b.y, b.x))
    return pruned


def ocr_bubble(img_bgr: np.ndarray, bubble: Bubble) -> str:
    h, w = img_bgr.shape[:2]
    pad = 10
    x1 = max(0, bubble.x - pad)
    y1 = max(0, bubble.y - pad)
    x2 = min(w, bubble.x + bubble.w + pad)
    y2 = min(h, bubble.y + bubble.h + pad)

    crop = img_bgr[y1:y2, x1:x2]
    crop_thr = preprocess_bubble_for_ocr(crop, bubble.sender)

    txt = pytesseract.image_to_string(crop_thr, config="--oem 3 --psm 6")
    txt = txt.replace("\n", " ")
    txt = re.sub(r"\s+", " ", txt).strip()

    txt = re.sub(r"\bText Message\b.*?\bSMS\b", "", txt, flags=re.IGNORECASE).strip()
    txt = re.sub(r"\s*[+©]+\s*$", "", txt).strip()

    return txt


def is_ui_artifact_message(msg: str) -> bool:
    s = msg.strip()
    if not s:
        return True
    # Common header artifacts we don't want as messages
    if re.search(r"^(Jaguar - Los Angeles|Maybe: Robert)\s*>", s, re.IGNORECASE):
        return True
    # Timestamp-only / navigation fragments
    if re.search(r"^—\s*[A-Za-z]{3}\s+\d{1,2},\s+\d{4}\s+at\s+\d{1,2}:\d{2}", s, re.IGNORECASE):
        return True
    if re.fullmatch(r"(Today|Yesterday)\s+\d{1,2}:\d{2}\s*(AM|PM)", s, re.IGNORECASE):
        return True
    if re.fullmatch(r"(Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday)\s+\d{1,2}:\d{2}\s*(AM|PM)", s, re.IGNORECASE):
        return True
    # Generic contact header “Text Message · SMS”
    if re.search(r"Text Message\s*·\s*SMS", s, re.IGNORECASE):
        return True
    return False


def assign_timestamps(
    bubbles: List[Bubble],
    timestamp_lines: List[TimestampLine],
    screenshot_dt: datetime,
) -> List[Tuple[Bubble, datetime, bool]]:
    """Assign each bubble a timestamp (datetime)."""

    parsed: List[Tuple[int, datetime]] = []
    for t in timestamp_lines:
        dt = parse_timestamp_text(t.raw_text, screenshot_dt)
        if dt:
            parsed.append((t.y_center, dt))

    parsed.sort(key=lambda x: x[0])

    if not parsed:
        fallback = screenshot_dt.replace(hour=12, minute=0, second=0, microsecond=0)
        return [(b, fallback, True) for b in bubbles]

    result: List[Tuple[Bubble, datetime, bool]] = []
    idx = 0
    current_dt = parsed[0][1]
    used_count_for_current = 0

    for b in sorted(bubbles, key=lambda bb: bb.top):
        while idx + 1 < len(parsed) and parsed[idx + 1][0] < b.top:
            idx += 1
            current_dt = parsed[idx][1]
            used_count_for_current = 0

        approx = used_count_for_current > 0
        used_count_for_current += 1
        result.append((b, current_dt, approx))

    return result


def normalize_message_text(s: str) -> str:
    s = s.strip()
    s = re.sub(r"\s+", " ", s)
    return s


def transcript_sort_key(item: Dict) -> datetime:
    ts = item.get("timestamp") or ""
    ts = ts.replace(" (approx)", "")
    try:
        return datetime.strptime(ts, "%a, %b %d, %Y, %I:%M %p")
    except Exception:
        return datetime.min


def process_image(image_path: str) -> List[Dict]:
    img = cv2.imread(image_path)
    if img is None:
        return []

    screenshot_dt = get_screenshot_datetime(image_path)
    ts_lines = extract_timestamp_lines(img)
    bubbles = find_bubbles(img)
    assigned = assign_timestamps(bubbles, ts_lines, screenshot_dt)

    messages: List[Dict] = []
    for bubble, dt, approx in assigned:
        msg = ocr_bubble(img, bubble)
        msg = normalize_message_text(msg)
        if not msg or is_ui_artifact_message(msg):
            continue

        messages.append(
            {
                "timestamp": format_timestamp(dt, approx=approx),
                "sender": bubble.sender,
                "message": msg,
            }
        )

    return messages


def process_folder(folder_path: str) -> List[Dict]:
    image_exts = {".png", ".jpg", ".jpeg", ".PNG", ".JPG", ".JPEG"}
    paths = [
        os.path.join(folder_path, f)
        for f in os.listdir(folder_path)
        if Path(f).suffix in image_exts
    ]
    paths.sort()

    all_msgs: List[Dict] = []
    for p in paths:
        print(f"Processing {Path(p).name}")
        all_msgs.extend(process_image(p))

    return all_msgs


def dedupe(messages: Iterable[Dict]) -> List[Dict]:
    seen = set()
    out: List[Dict] = []

    for m in messages:
        ts = (m.get("timestamp") or "").strip()
        # When multiple bubbles share the same visible timestamp line, we mark them (approx).
        # For deduping, treat exact same message+sender at the same moment as identical.
        ts_key = ts.replace(" (approx)", "")
        sender = (m.get("sender") or "").strip()
        msg = normalize_message_text(m.get("message") or "")
        if not msg:
            continue
        key = (ts_key, sender, msg)
        if key in seen:
            continue
        seen.add(key)
        out.append({"timestamp": ts, "sender": sender, "message": msg})

    return out


def main() -> None:
    base_dir = Path(__file__).parent

    older = base_dir / "Older Text"
    woodland = base_dir / "Jag Woodland Texts"

    all_msgs: List[Dict] = []

    if older.exists():
        all_msgs.extend(process_folder(str(older)))
    if woodland.exists():
        all_msgs.extend(process_folder(str(woodland)))

    all_msgs = dedupe(all_msgs)
    all_msgs.sort(key=transcript_sort_key)

    out_path = base_dir / "transcript.json"
    out_path.write_text(json.dumps(all_msgs, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"\nWrote {len(all_msgs)} messages to {out_path}")


if __name__ == "__main__":
    main()
