#!/usr/bin/env python3
"""
Scrape CarComplaints.com for Jaguar TSB PDF URLs and download them
"""

import requests
import re
import os
from urllib.parse import urljoin

def extract_tsb_urls_from_file(filename):
    """Extract TSB detail page URLs from the CarComplaints markdown file"""
    urls = []
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all TSB detail page links
    pattern = r'\[Read More »\]\((/Jaguar/S-TYPE/2004/tsbs/[^)]+\.shtml)\)'
    matches = re.findall(pattern, content)
    
    # Convert relative URLs to absolute
    base_url = "https://www.carcomplaints.com"
    for match in matches:
        urls.append(urljoin(base_url, match))
    
    return urls

def extract_pdf_url_from_page(tsb_url):
    """Extract the PDF download URL from a TSB detail page"""
    try:
        response = requests.get(tsb_url, timeout=10)
        if response.status_code == 200:
            # Look for NHTSA PDF links
            pdf_pattern = r'href="(https://static\.nhtsa\.gov/odi/tsbs/[^"]*\.pdf)"'
            match = re.search(pdf_pattern, response.text)
            if match:
                return match.group(1)
    except Exception as e:
        print(f"Error fetching {tsb_url}: {e}")
    
    return None

def download_pdf(pdf_url, output_dir="tsb_pdfs"):
    """Download a PDF from the given URL"""
    try:
        response = requests.get(pdf_url, timeout=15)
        if response.status_code == 200 and 'application/pdf' in response.headers.get('content-type', ''):
            # Extract filename from URL
            filename = pdf_url.split('/')[-1]
            filepath = os.path.join(output_dir, f"carcomplaints_{filename}")
            
            with open(filepath, 'wb') as f:
                f.write(response.content)
            
            print(f"✓ Downloaded: {filename}")
            return True
    except Exception as e:
        print(f"Error downloading {pdf_url}: {e}")
    
    return False

def main():
    """Main scraping and download function"""
    os.makedirs("tsb_pdfs", exist_ok=True)
    
    # Extract TSB detail page URLs
    tsb_urls = extract_tsb_urls_from_file("www.carcomplaints.comjaguar-s-type-2004-tsbs.md")
    print(f"Found {len(tsb_urls)} TSB detail pages")
    
    # Process first 10 TSBs
    downloaded = 0
    for i, tsb_url in enumerate(tsb_urls[:10]):
        print(f"\nProcessing TSB {i+1}/10: {tsb_url}")
        
        # Extract PDF URL from detail page
        pdf_url = extract_pdf_url_from_page(tsb_url)
        if pdf_url:
            print(f"Found PDF URL: {pdf_url}")
            if download_pdf(pdf_url):
                downloaded += 1
        else:
            print("No PDF URL found on this page")
    
    print(f"\nDownloaded {downloaded} out of {min(10, len(tsb_urls))} TSB PDFs")

if __name__ == "__main__":
    main()
