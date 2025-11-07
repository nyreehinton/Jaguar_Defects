#!/usr/bin/env python3
"""
Scrape CarComplaints.com for Jaguar TSB PDF URLs and download them
"""

import requests
import re
import os
import sys
from urllib.parse import urljoin

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

def extract_tsb_urls_from_file(filename):
    """Extract TSB detail page URLs from the CarComplaints markdown file"""
    urls = []
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find the model path from filename, e.g., 'f-type-2020' -> 'F-TYPE/2020'
    basename = os.path.basename(filename).replace('.md', '')
    # Extract model and year
    # Assuming format www.carcomplaints.comjaguar-{model}-{year}-tsbs.md
    parts = basename.split('jaguar-')
    if len(parts) > 1:
        model_year_str = parts[1].replace('-tsbs', '')
        hyphens = model_year_str.split('-')
        if len(hyphens) >= 2:
            year = hyphens[-1]
            model = '-'.join(hyphens[:-1]).upper()
            model_path = f"/Jaguar/{model}/{year}/tsbs/"
        else:
            model_path = "/Jaguar/F-TYPE/2020/tsbs/"  # default
    else:
        model_path = "/Jaguar/F-TYPE/2020/tsbs/"  # default
    
    # Find all TSB detail page links using the model path
    pattern = rf'\[Read More »\]\(({re.escape(model_path)}[^)]+\.shtml)\)'  # Capture group for the URL
    matches = re.findall(pattern, content)
    
    # Convert relative URLs to absolute
    base_url = "https://www.carcomplaints.com"
    for match in matches:
        urls.append(urljoin(base_url, match))
    
    return urls

def extract_pdf_url_from_page(tsb_url):
    """Extract the PDF download URL from a TSB detail page"""
    try:
        response = requests.get(tsb_url, headers=headers, timeout=10)
        print(f"Status for {tsb_url}: {response.status_code}")
        if response.status_code == 200:
            text = response.text
            print(f"Page length: {len(text)} chars")
            # Debug: check if pdf mentioned
            if 'pdf' in text.lower():
                print(f"PDF mentioned in {tsb_url.split('/')[-1]}")
                # Find TSB Document section
                doc_section = re.search(r'TSB Document.*?href="([^"]*\.pdf[^"]*)"', text, re.DOTALL | re.IGNORECASE)
                if doc_section:
                    pdf_url = doc_section.group(1)
                    if not pdf_url.startswith('http'):
                        pdf_url = urljoin(tsb_url, pdf_url)
                    print(f"Found PDF in doc section: {pdf_url}")
                    return pdf_url
                # Print snippet around 'TSB Document'
                tsb_doc_pos = text.lower().find('tsb document')
                if tsb_doc_pos != -1:
                    snippet_start = max(0, tsb_doc_pos - 100)
                    snippet_end = min(len(text), tsb_doc_pos + 300)
                    print(f"Snippet around TSB Document: {repr(text[snippet_start:snippet_end])}")
            else:
                print(f"No PDF mentioned in {tsb_url.split('/')[-1]}")
            
            # Original patterns
            pdf_pattern = r'href="(https://static\.nhtsa\.gov/odi/tsbs/[^"]*SB-[^"]*\.pdf)"'
            match = re.search(pdf_pattern, text)
            if match:
                return match.group(1)
            
            alt_pattern = r'<li><a[^>]*href="([^"]*\.pdf)"[^>]*title="([^"]*\.pdf)"'
            match = re.search(alt_pattern, text)
            if match:
                pdf_url = match.group(1)
                if not pdf_url.startswith('http'):
                    pdf_url = urljoin(tsb_url, pdf_url)
                return pdf_url
        else:
            print(f"Failed to fetch {tsb_url}: status {response.status_code}")
    except Exception as e:
        print(f"Error fetching {tsb_url}: {e}")
    
    return None

def download_pdf(pdf_url, output_dir="tsb_pdfs"):
    """Download a PDF from the given URL"""
    try:
        response = requests.get(pdf_url, headers=headers, timeout=15)
        if response.status_code == 200:
            # Extract filename from URL
            filename = pdf_url.split('/')[-1]
            filepath = os.path.join(output_dir, f"carcomplaints_{filename}")
            
            # Skip if already exists
            if os.path.exists(filepath):
                print(f"Already exists: {filename}")
                return True
            
            with open(filepath, 'wb') as f:
                f.write(response.content)
            
            # Verify it's actually a PDF
            if b'%PDF' in response.content[:100]:
                print(f"✓ Downloaded PDF: {filename}")
                return True
            else:
                print(f"✗ Downloaded file is not a PDF: {filename}")
                os.remove(filepath)  # Remove invalid file
                return False
    except Exception as e:
        print(f"Error downloading {pdf_url}: {e}")
    
    return False

def main(md_filename=None):
    """Main scraping and download function"""
    if md_filename is None:
        if len(sys.argv) > 1:
            md_filename = sys.argv[1]
        else:
            print("Usage: python3 scrape_carcomplaints_pdfs_fixed.py <md_filename>")
            return
    
    os.makedirs("tsb_pdfs", exist_ok=True)
    
    # Extract TSB detail page URLs
    tsb_urls = extract_tsb_urls_from_file(md_filename)
    print(f"Found {len(tsb_urls)} TSB detail pages")
    
    # Process all TSBs
    downloaded = 0
    total_processed = 0
    for i, tsb_url in enumerate(tsb_urls):  # Process all
        print(f"\nProcessing TSB {i+1}/{len(tsb_urls)}: {tsb_url.split('/')[-1]}")
        
        # Extract PDF URL from detail page
        pdf_url = extract_pdf_url_from_page(tsb_url)
        if pdf_url:
            print(f"Found PDF URL: {pdf_url.split('/')[-1]}")
            if download_pdf(pdf_url):
                downloaded += 1
        else:
            print("No PDF URL found on this page")
        total_processed += 1
    
    print(f"\nDownloaded {downloaded} out of {total_processed} TSB PDFs")

if __name__ == "__main__":
    main()
