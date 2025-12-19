# File Structure

## Field 1: NHTSA ID Number (NUMBER(9))

## Field 2: Replacement Service Bulletin Number (CHAR(16))

## Field 3: Date Added to File (DATE - YYYYMMDD)

## Field 4: TSB/Document ID (CHAR(128)) - This is the main identifier we're looking for

## Field 5: Mfr Communication Date (DATE - YYYYMMDD)

## Field 6: Mfr Internal Campaign ID/Software Version (CHAR(128))

## Field 7: Communication Type (CHAR(40))

## Field 8: Make (CHAR(25))

## Field 9: Model (CHAR(40))

## Field 10: Model Year (CHAR(4))

## Field 11: NHTSA Components (CHAR(256))

## Field 12: Mfr Component System (CHAR(256))

## Field 13: Mfr Component Subsystem (CHAR(256))

## Field 14: Summary (CHAR(4000))

## Key Points

- The files are tab-separated
- Each line represents one record
- The TSB/Document ID (Field 4) is what we should search for
- The files contain data from all manufacturers, not just Jaguar
- Recent Changes (as of May 2024):
  - Field names were updated for clarity
  - Field lengths were adjusted
  - The file format remains tab-separated
