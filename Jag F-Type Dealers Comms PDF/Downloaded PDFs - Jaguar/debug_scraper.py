#!/usr/bin/env python3
"""
Debug the PDF URL extraction
"""

import requests
import re

def debug_pdf_extraction():
    """Debug PDF URL extraction from CarComplaints page"""
    url = "https://www.carcomplaints.com/Jaguar/S-TYPE/2004/tsbs/tsb-jtb00208nas2.shtml"
    
    print(f"Fetching: {url}")
    response = requests.get(url, timeout=10)
    print(f"Status: {response.status_code}")
    print(f"Content length: {len(response.text)}")
    
    # Look for the TSB Document section
    if "TSB Document" in response.text:
        print("✓ Found 'TSB Document' section")
        
        # Extract the section
        start = response.text.find("TSB Document")
        end = response.text.find("</h3>", start) + 5
        section = response.text[start:end]
        print(f"Section: {section}")
        
        # Try regex patterns
        patterns = [
            r'href="(https://static\.nhtsa\.gov/odi/tsbs/[^"]*\.pdf)"',
            r'href="([^"]*\.pdf)"',
            r'https://static\.nhtsa\.gov[^"]*\.pdf'
        ]
        
        for i, pattern in enumerate(patterns):
            matches = re.findall(pattern, response.text)
            print(f"Pattern {i+1} matches: {matches}")
    else:
        print("✗ 'TSB Document' section not found")

if __name__ == "__main__":
    debug_pdf_extraction()
