#!/usr/bin/env python3
import json, time, sys
import requests

BASE = "https://api.nhtsa.gov"
YEAR = 2025
OUTFILE = "recalls_2025.json"

def get(url, **params):
    r = requests.get(url, params=params, timeout=20)
    r.raise_for_status()
    return r.json().get("results", [])

print(f"Fetching makes for {YEAR} recalls …")
# Use lower-case versions of makes to satisfy the case-sensitive recalls endpoint
makes = [m["make"].lower() for m in get(f"{BASE}/products/vehicle/makes",
                                 modelYear=YEAR, issueType="r")]
print(f"  {len(makes)} makes found")

all_recalls = []
for idx, make in enumerate(makes, 1):
    try:
        models = sorted({m["model"].lower() for m in get(f"{BASE}/products/vehicle/models",
                                          modelYear=YEAR, make=make,
                                          issueType="r")})  # set → deduplicate & sort
    except requests.HTTPError as e:
        print(f"! Failed to pull models for {make}: {e.response.status_code} — skipped")
        continue
    print(f"[{idx:3}/{len(makes)}] {make}: {len(models)} models")
    for model in models:
        try:
            recalls = get(f"{BASE}/recalls/recallsByVehicle",
                          make=make, model=model, modelYear=YEAR)
        except requests.HTTPError as e:
            # Skip combos the API rejects (usually no data); continue
            print(f"      ! {model}: {e.response.status_code} — skipped")
            continue
        if recalls:
            all_recalls.extend(recalls)
            print(f"      ↳ {model}: {len(recalls)} recalls")

        # Be polite to the API
        time.sleep(0.15)

print(f"\nTotal recall records collected: {len(all_recalls)}")

# Deduplicate (same campaigns can repeat across trims)
seen = set()
unique_recalls = []
for rec in all_recalls:
    key = rec["NHTSACampaignNumber"]
    if key not in seen:
        seen.add(key)
        unique_recalls.append(rec)

print(f"Unique campaigns: {len(unique_recalls)}")

with open(OUTFILE, "w") as fp:
    json.dump(unique_recalls, fp, indent=2)

print(f"Saved to {OUTFILE}")