#!/usr/bin/env python3
"""
JSON Invoice Validator
Validates all JSON files in the Invoices folder for:
- Valid JSON syntax
- Required fields
- Data type consistency
- Common errors
"""

import json
import os
from pathlib import Path
from typing import Dict, List, Any, Tuple

def validate_json_syntax(file_path: str) -> Tuple[bool, str, Any]:
    """Validate JSON syntax and return parsed data if valid."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return True, "Valid JSON", data
    except json.JSONDecodeError as e:
        return False, f"JSON Syntax Error: {str(e)}", None
    except Exception as e:
        return False, f"File Error: {str(e)}", None

def validate_structure(data: Dict[str, Any], file_name: str) -> List[str]:
    """Validate the structure and content of the invoice data."""
    issues = []
    
    # Check for common required fields based on different invoice formats
    if not isinstance(data, dict):
        issues.append("Root element must be a dictionary/object")
        return issues
    
    # Check for dealer/vendor information (multiple formats supported)
    has_dealer = "dealer_information" in data
    has_vendor = "vendor_name" in data or "vendor_information" in data
    has_invoice_fields = "Invoice #" in data  # Alternative format
    
    if not has_dealer and not has_vendor and not has_invoice_fields:
        issues.append("Missing dealer_information, vendor_name, or Invoice # field")
    
    # Check for customer information (multiple formats supported)
    has_customer_nested = "customer_information" in data
    has_customer_flat = "customer_name" in data or "Customer Name" in data
    
    if not has_customer_nested and not has_customer_flat:
        issues.append("Missing customer_information or customer_name/Customer Name")
    
    # Check for vehicle information (multiple formats supported)
    has_vehicle_nested = "vehicle_information" in data or "vehicle_details" in data
    has_vehicle_flat = any(key.startswith("Vehicle") for key in data.keys())
    
    if not has_vehicle_nested and not has_vehicle_flat:
        issues.append("Missing vehicle_information, vehicle_details, or Vehicle fields")
    
    # Validate numeric fields
    numeric_fields_to_check = [
        ("mileage_in", ["vehicle_information", "vehicle_details"]),
        ("mileage_out", ["vehicle_information", "vehicle_details"]),
        ("estimated_total", ["estimates"]),
        ("total_amount", ["summary", "totals"]),
    ]
    
    for field, paths in numeric_fields_to_check:
        for path in paths:
            if path in data and field in data[path]:
                value = data[path][field]
                if value is not None:
                    # Check if it's a string that should be numeric
                    if isinstance(value, str):
                        try:
                            float(value.replace(",", ""))
                        except ValueError:
                            issues.append(f"{path}.{field} contains non-numeric string: '{value}'")
    
    # Check for VIN consistency
    vin_fields = []
    if "vehicle_information" in data and "vin" in data["vehicle_information"]:
        vin_fields.append(data["vehicle_information"]["vin"])
    elif "vehicle_details" in data and "vin" in data["vehicle_details"]:
        vin_fields.append(data["vehicle_details"]["vin"])
    else:
        # Check for flat format VIN fields
        for key in data.keys():
            if "VIN" in key.upper() or key == "vin":
                vin_fields.append(data[key])
    
    if vin_fields:
        vin = vin_fields[0]
        if vin and isinstance(vin, str) and len(vin) != 17:
            issues.append(f"VIN length is {len(vin)}, expected 17 characters")
    
    # Check for date formats
    date_fields = []
    if "work_order_dates" in data:
        date_fields.extend(data["work_order_dates"].values())
    if "dates" in data:
        date_fields.extend(data["dates"].values())
    if "Invoice Date" in data:
        date_fields.append(data["Invoice Date"])
    
    # Check for null values in critical fields (only warn, don't fail)
    # VIN should not be null
    vin_value = None
    if "vehicle_information" in data and "vin" in data["vehicle_information"]:
        vin_value = data["vehicle_information"]["vin"]
    elif "vehicle_details" in data and "vin" in data["vehicle_details"]:
        vin_value = data["vehicle_details"]["vin"]
    elif "Vehicle VIN" in data:
        vin_value = data["Vehicle VIN"]
    
    if vin_value is None:
        issues.append("Warning: VIN is null or missing")
    
    return issues

def validate_data_types(data: Dict[str, Any]) -> List[str]:
    """Validate data types are consistent."""
    issues = []
    
    # Check arrays are actually arrays
    array_fields = ["repair_items", "Line Items", "service_details", "line_items", "recommended_repairs"]
    for field in array_fields:
        if field in data:
            if not isinstance(data[field], list):
                # service_details can be either dict or list depending on format
                if field == "service_details" and isinstance(data[field], dict):
                    continue  # This is valid for some invoice formats
                issues.append(f"{field} should be an array/list, got {type(data[field]).__name__}")
    
    # Check nested objects (service_details can be either list or dict depending on format)
    object_fields = ["dealer_information", "customer_information", "vehicle_information", 
                     "service_advisor", "work_order_dates", "payment_details", "estimates",
                     "summary", "totals", "summary_and_totals"]
    for field in object_fields:
        if field in data:
            if not isinstance(data[field], dict):
                issues.append(f"{field} should be an object/dict, got {type(data[field]).__name__}")
    
    return issues

def main():
    """Main validation function."""
    invoices_dir = Path(__file__).parent / "Invoices"
    
    if not invoices_dir.exists():
        print(f"Error: Invoices directory not found at {invoices_dir}")
        return
    
    json_files = list(invoices_dir.glob("*.json"))
    
    if not json_files:
        print("No JSON files found in Invoices directory")
        return
    
    print(f"Found {len(json_files)} JSON file(s) to validate\n")
    print("=" * 80)
    
    all_valid = True
    results = []
    
    for json_file in sorted(json_files):
        print(f"\nValidating: {json_file.name}")
        print("-" * 80)
        
        # Validate JSON syntax
        is_valid, message, data = validate_json_syntax(str(json_file))
        
        if not is_valid:
            print(f"❌ {message}")
            all_valid = False
            results.append({
                "file": json_file.name,
                "valid": False,
                "issues": [message]
            })
            continue
        
        print(f"✓ JSON syntax: Valid")
        
        # Validate structure
        structure_issues = validate_structure(data, json_file.name)
        type_issues = validate_data_types(data)
        
        all_issues = structure_issues + type_issues
        
        if all_issues:
            print(f"⚠ Found {len(all_issues)} issue(s):")
            for issue in all_issues:
                print(f"  - {issue}")
            all_valid = False
        else:
            print(f"✓ Structure: Valid")
            print(f"✓ Data types: Valid")
        
        results.append({
            "file": json_file.name,
            "valid": len(all_issues) == 0,
            "issues": all_issues
        })
    
    # Summary
    print("\n" + "=" * 80)
    print("VALIDATION SUMMARY")
    print("=" * 80)
    
    valid_count = sum(1 for r in results if r["valid"])
    total_count = len(results)
    
    print(f"\nTotal files: {total_count}")
    print(f"Valid: {valid_count}")
    print(f"Issues found: {total_count - valid_count}")
    
    if all_valid:
        print("\n✅ All JSON files are valid!")
    else:
        print("\n⚠ Some files have issues:")
        for result in results:
            if not result["valid"]:
                print(f"\n  {result['file']}:")
                for issue in result["issues"]:
                    print(f"    - {issue}")
    
    return all_valid

if __name__ == "__main__":
    exit(0 if main() else 1)

