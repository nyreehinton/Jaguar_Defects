#!/usr/bin/env python3
"""
Jaguar TSB PDF Downloader

This script attempts to download Jaguar Technical Service Bulletins (TSBs)
from various automotive service websites.
"""

import requests
import os
from pathlib import Path

# List of bulletin IDs from the TSB file
BULLETIN_IDS = [
    "H419", "H428", "H451", "H451v3", "H474", "H490v2", "H524", "H525", "H538",
    "JLRTB02128NAS", "SSM76240", "SSM76231", "SSM76257", "SSM76258", "SSM76268",
    "SSM76281", "SSM76302", "SSM76314", "SSM76318", "SSM76320", "SSM76332",
    "SSM76342", "SSM76318ATT", "SSM76318ATT1", "SSM76318ATT2", "SSM76318ATT3"
]

# Potential TSB hosting sites
TSB_SOURCES = [
    "https://static.nhtsa.gov/odi/tsbs/2025/{}.pdf",
    "https://static.nhtsa.gov/odi/tsbs/jaguar/{}.pdf", 
    "https://www.alldatadiy.com/tsb/jaguar/{}.pdf",
    "https://www.realoem.com/tsb/jaguar/{}.pdf",
    "https://workshopmanuals.com/tsb/jaguar/{}.pdf",
    "https://tsb.epc-data.com/tsb/jaguar/{}.pdf",
    "https://www.automotivedata.com/tsb/jaguar/{}.pdf"
]

def download_tsb(bulletin_id, source_url_template, output_dir="tsb_pdfs"):
    """Download a TSB PDF from a specific source"""
    url = source_url_template.format(bulletin_id)
    filename = f"{bulletin_id}_{source_url_template.split('/')[2].replace('www.', '').replace('.', '_')}.pdf"
    filepath = os.path.join(output_dir, filename)
    
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            # Check if it's actually a PDF
            content_type = response.headers.get('content-type', '')
            if 'pdf' in content_type.lower() or 'application/pdf' in content_type:
                with open(filepath, 'wb') as f:
                    f.write(response.content)
                print(f"✓ Downloaded PDF: {filename}")
                return True
            else:
                # Save anyway in case it's a redirect or embedded PDF
                with open(filepath, 'wb') as f:
                    f.write(response.content)
                print(f"? Downloaded (not PDF): {filename}")
                return False
    except Exception as e:
        print(f"✗ Failed to download {bulletin_id} from {url.split('/')[2]}: {e}")
    
    return False

def main():
    """Main download function"""
    output_dir = "tsb_pdfs"
    os.makedirs(output_dir, exist_ok=True)
    
    successful_downloads = []
    
    print("Starting Jaguar TSB PDF download...")
    print("=" * 50)
    
    for bulletin_id in BULLETIN_IDS[:5]:  # Try first 5 bulletins
        print(f"\nTrying bulletin: {bulletin_id}")
        
        for source_template in TSB_SOURCES:
            if download_tsb(bulletin_id, source_template, output_dir):
                successful_downloads.append((bulletin_id, source_template))
                break  # Found one, move to next bulletin
    
    print(f"\n{'='*50}")
    print(f"Download complete. Found {len(successful_downloads)} PDFs")
    
    if successful_downloads:
        print("\nSuccessful downloads:")
        for bulletin, source in successful_downloads:
            print(f"  {bulletin}: {source.split('/')[2]}")
    
    print("\nNote: Many sites return HTML pages instead of direct PDFs.")
    print("You may need to check the downloaded files and extract PDFs manually.")

if __name__ == "__main__":
    main()
