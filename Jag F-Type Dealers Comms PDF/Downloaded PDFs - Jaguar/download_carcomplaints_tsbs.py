#!/usr/bin/env python3
"""
Download Jaguar TSBs using NHTSA IDs from CarComplaints data
"""

import requests
import re
import os

def extract_nhtsa_ids(filename):
    """Extract NHTSA IDs from the CarComplaints markdown file"""
    ids = []
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all NHTSA ID patterns
    pattern = r'NHTSA ID:\s*\n\s*#(\d+)'
    matches = re.findall(pattern, content)
    return list(set(matches))  # Remove duplicates

def try_download_tsb(nhtsa_id):
    """Try different URL patterns to download a TSB"""
    base_id = nhtsa_id
    
    # Try different year ranges (2000-2025)
    for year in range(2000, 2026):
        # Try different suffix patterns based on the ID
        suffixes = [
            base_id[-4:],  # Last 4 digits
            base_id[-3:],  # Last 3 digits  
            base_id[-2:],  # Last 2 digits
            str(int(base_id) % 10000),  # ID mod 10000
            str(int(base_id) % 1000),   # ID mod 1000
        ]
        
        for suffix in suffixes:
            url = f"https://static.nhtsa.gov/odi/tsbs/{year}/SB-{base_id}-{suffix}.pdf"
            try:
                response = requests.head(url, timeout=5)
                if response.status_code == 200:
                    # Download the PDF
                    response = requests.get(url, timeout=10)
                    filename = f"tsb_pdfs/carcomplaints_{base_id}_{year}_{suffix}.pdf"
                    with open(filename, 'wb') as f:
                        f.write(response.content)
                    print(f"✓ Downloaded: {filename}")
                    return True
            except:
                continue
    
    return False

def main():
    """Main download function"""
    os.makedirs("tsb_pdfs", exist_ok=True)
    
    # Extract NHTSA IDs from CarComplaints file
    nhtsa_ids = extract_nhtsa_ids("www.carcomplaints.comjaguar-s-type-2004-tsbs.md")
    print(f"Found {len(nhtsa_ids)} unique NHTSA IDs")
    
    # Try to download first 10 TSBs
    downloaded = 0
    for nhtsa_id in nhtsa_ids[:10]:
        print(f"Trying NHTSA ID: {nhtsa_id}")
        if try_download_tsb(nhtsa_id):
            downloaded += 1
        else:
            print(f"✗ No PDF found for ID: {nhtsa_id}")
    
    print(f"\nDownloaded {downloaded} out of {min(10, len(nhtsa_ids))} TSBs")

if __name__ == "__main__":
    main()
