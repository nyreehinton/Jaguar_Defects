#!/usr/bin/env python3
"""
Debug the actual page content
"""

import requests

def debug_content():
    """Debug what content we get from CarComplaints"""
    url = "https://www.carcomplaints.com/Jaguar/S-TYPE/2004/tsbs/tsb-jtb00208nas2.shtml"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
    }
    
    response = requests.get(url, headers=headers, timeout=15)
    print(f"Status: {response.status_code}")
    print(f"Content length: {len(response.text)}")
    
    # Check for TSB Document section
    if "TSB Document" in response.text:
        print("✓ Found 'TSB Document' section")
        
        # Find the section
        start = response.text.find("TSB Document")
        end = response.text.find("</h3>", start)
        if end > 0:
            section = response.text[start:end+5]
            print(f"TSB Section: {section}")
        else:
            print("Could not find end of section")
    else:
        print("✗ 'TSB Document' section not found")
        # Show a sample of the content
        print(f"First 500 chars: {response.text[:500]}")

if __name__ == "__main__":
    debug_content()
