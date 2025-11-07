#!/bin/bash

# List of sites to try
SITES=(
    "https://static.nhtsa.gov/odi/tsbs/"
    "https://www.alldatadiy.com/tsb/jaguar/"
    "https://www.realoem.com/tsb/jaguar/"
    "https://workshopmanuals.com/tsb/jaguar/"
)

# Bulletin IDs to try
BULLETINS=("H419" "H428" "H451")

for site in "${SITES[@]}"; do
    for bulletin in "${BULLETINS[@]}"; do
        url="${site}${bulletin}.pdf"
        output_file="tsb_pdfs/${bulletin}_$(basename "$site" .com | sed 's/www\.//').pdf"
        
        echo "Trying: $url"
        if curl -s -L "$url" -o "$output_file" 2>/dev/null; then
            if file "$output_file" | grep -q "PDF document"; then
                echo "SUCCESS: Found PDF for $bulletin at $site"
                ls -la "$output_file"
                exit 0
            fi
        fi
    done
done

echo "No working PDF sources found"
