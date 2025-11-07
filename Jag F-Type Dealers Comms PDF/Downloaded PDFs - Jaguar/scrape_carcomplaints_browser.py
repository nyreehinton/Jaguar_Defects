#!/usr/bin/env python3
"""
Scrape CarComplaints.com for Jaguar TSB PDF URLs using browser-like headers
"""

import requests
import re
import os

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
        urls.append(base_url + match)
    
    return urls

def extract_pdf_url_from_page(tsb_url):
    """Extract the PDF download URL from a TSB detail page"""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
    }
    
    try:
        response = requests.get(tsb_url, headers=headers, timeout=15)
        print(f"Status: {response.status_code}")
        
        if response.status_code == 200:
            # Look for NHTSA PDF links
            pdf_pattern = r'href="(https://static\.nhtsa\.gov/odi/tsbs/[^"]*\.pdf)"'
            match = re.search(pdf_pattern, response.text)
            if match:
                return match.group(1)
            
            # Alternative: look for any PDF links
            alt_pattern = r'href="([^"]*\.pdf)"'
            matches = re.findall(alt_pattern, response.text)
            nhtsa_matches = [m for m in matches if 'nhtsa.gov' in m]
            if nhtsa_matches:
                return nhtsa_matches[0]
                
    except Exception as e:
        print(f"Error: {e}")
    
    return None

def download_pdf(pdf_url, output_dir="tsb_pdfs"):
    """Download a PDF from the given URL"""
    try:
        response = requests.get(pdf_url, timeout=15)
        if response.status_code == 200 and b'%PDF' in response.content[:100]:
            # Extract filename from URL
            filename = pdf_url.split('/')[-1]
            filepath = os.path.join(output_dir, f"carcomplaints_{filename}")
            
            with open(filepath, 'wb') as f:
                f.write(response.content)
            
            print(f"✓ Downloaded: {filename}")
            return True
    except Exception as e:
        print(f"Download error: {e}")
    
    return False

def main():
    """Main scraping and download function"""
    os.makedirs("tsb_pdfs", exist_ok=True)
    
    # Extract TSB detail page URLs
    tsb_urls = extract_tsb_urls_from_file("www.carcomplaints.comjaguar-s-type-2004-tsbs.md")
    print(f"Found {len(tsb_urls)} TSB detail pages")
    
    # Test just the first few
    downloaded = 0
    for i, tsb_url in enumerate(tsb_urls[:3]):
        print(f"\nProcessing TSB {i+1}: {tsb_url.split('/')[-1]}")
        
        # Extract PDF URL from detail page
        pdf_url = extract_pdf_url_from_page(tsb_url)
        if pdf_url:
            print(f"Found PDF: {pdf_url}")
            if download_pdf(pdf_url):
                downloaded += 1
        else:
            print("No PDF found")
    
    print(f"\nDownloaded {downloaded} PDFs")

if __name__ == "__main__":
    main()
