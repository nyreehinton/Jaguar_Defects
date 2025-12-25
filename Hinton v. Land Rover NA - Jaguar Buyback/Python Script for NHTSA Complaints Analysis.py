# @title GEMINI Version 2 - Expanded Analysis
import pandas as pd
import re
from datetime import datetime
from collections import Counter
import os # For path joining

# --- Configuration & Keywords ---
NARRATIVE_COLUMNS = ['COMPDESC', 'CDESCR']
JLR_MFR_NAMES = ['Jaguar', 'Land Rover'] # MFR_NAME in CSV
VEHICLE_MAKES_FOR_REPORT = ['JAGUAR', 'LAND ROVER'] # MAKETXT in CSV for make/model counts

ELECTRICAL_KEYWORDS = [
    "door module", "window switch", "blown fuse", "short to ground", "harness",
    "junction box", "C13H", "U3003-16", "battery failure", "electrical problem",
    "wiring", "control module", "infotainment", "sensor"
]
COOLING_KEYWORDS = [
    "coolant leak", "expansion tank", "bleed pipe", "low coolant warning", "overheat",
    "water pump", "thermostat", "radiator", "cooling system"
]
# Regex for finding dates - intentionally broad to capture various "literal text" formats
# Handles MM/DD/YY(YY), Month DD, YYYY, YYYY, etc.
DATE_REGEX = r'\b(?:\d{1,2}[-/]\d{1,2}[-/]\d{2,4}|(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)\s+\d{1,2}(?:st|nd|rd|th)?(?:,)?\s+\d{2,4}|\b\d{4})\b'

# --- Context for ACP Letter (Used in Sections 5 & 6) ---
ACP_CASE_REFERENCE = "JAG2501941"
ACP_VEHICLE_MODEL_YEAR = "2020 Jaguar F-Type"
ACP_KEY_ISSUES = "electrical and cooling system defects"
ACP_MMWA_RELEVANCE = "Magnuson-Moss Warranty Act (MMWA) applicability and BBB AUTO LINE's jurisdictional interpretations"

# --- Helper Functions ---

def load_data(file_path="/content/jaguar_complaints.csv"):
    """Loads the CSV data into a pandas DataFrame."""
    try:
        print(f"Attempting to load data from: {os.path.abspath(file_path)}")
        df = pd.read_csv(file_path, low_memory=False)
        print(f"Successfully loaded {file_path}. Shape: {df.shape}")
        # Ensure relevant text columns are strings and handle potential NaN values
        # CMPLID is crucial and should be string. YEARTXT too.
        cols_to_str = NARRATIVE_COLUMNS + ['MFR_NAME', 'MODELTXT', 'MAKETXT', 'CMPLID', 'YEARTXT']
        for col in cols_to_str:
            if col in df.columns:
                df[col] = df[col].astype(str).fillna('')
            else:
                print(f"Warning: Expected column '{col}' not found in the CSV.")
        return df
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found at {os.path.abspath(file_path)}.")
        return pd.DataFrame()
    except Exception as e:
        print(f"Error loading data from {file_path}: {e}")
        return pd.DataFrame()

def combine_narratives(row):
    """Combines COMPDESC and CDESCR fields safely."""
    # Ensure NARRATIVE_COLUMNS exist in the row (e.g. if df is subset)
    compdesc_val = str(row['COMPDESC']) if 'COMPDESC' in row and pd.notna(row['COMPDESC']) else ""
    cdescr_val = str(row['CDESCR']) if 'CDESCR' in row and pd.notna(row['CDESCR']) else ""
    return compdesc_val + " " + cdescr_val

def count_keyword_mentions(df, keywords_list):
    """Counts rows where keywords are mentioned in narrative columns (COMPDESC, CDESCR)."""
    if df.empty or not keywords_list:
        return 0
    
    # Ensure NARRATIVE_COLUMNS exist in the DataFrame
    valid_narrative_cols = [col for col in NARRATIVE_COLUMNS if col in df.columns]
    if not valid_narrative_cols:
        print("Warning: None of the specified NARRATIVE_COLUMNS found for keyword counting.")
        return 0

    # Combine specified narrative columns for searching
    # Fill NaN with empty string to prevent errors during concatenation or search
    # This creates a temporary series for the search operation
    narrative_search_series = df[valid_narrative_cols[0]].astype(str).fillna('')
    for i in range(1, len(valid_narrative_cols)):
        narrative_search_series += " " + df[valid_narrative_cols[i]].astype(str).fillna('')

    # Create a single regex pattern for all keywords (case-insensitive)
    # re.escape is important for keywords that might contain special regex characters
    pattern = '|'.join([re.escape(kw) for kw in keywords_list])
    
    # Count rows where the combined narrative contains any of the keywords
    # .na=False ensures that rows with NaN in the narrative (after fillna('')) are not matched if pattern is empty
    # but str.contains should handle them correctly as non-matches.
    return df[narrative_search_series.str.contains(pattern, case=False, na=False)].shape[0]


def get_narrative_exemplars(df, keywords_list, num_exemplars=5):
    """Gets the most narrative-rich complaints for a keyword bucket, based on CDESCR length."""
    if df.empty or not keywords_list:
        return []

    # Ensure required columns for processing and output exist
    required_cols_for_exemplars = NARRATIVE_COLUMNS + ['CMPLID', 'YEARTXT', 'MAKETXT', 'MODELTXT']
    if not all(col in df.columns for col in required_cols_for_exemplars):
        missing_cols = [col for col in required_cols_for_exemplars if col not in df.columns]
        print(f"Warning: Missing columns for exemplars: {missing_cols}. Cannot generate exemplars.")
        return []
    if 'CDESCR' not in df.columns: # Specifically needed for length sorting
        print("Warning: CDESCR column missing. Cannot sort exemplars by its length.")
        return []

    # Create a temporary DataFrame copy to add columns without modifying original df_complaints
    temp_df = df.copy()
    
    # Combine narrative columns for keyword searching
    temp_df['TEMP_FULL_NARRATIVE_FOR_SEARCH'] = temp_df.apply(combine_narratives, axis=1)
    
    pattern = '|'.join([re.escape(kw) for kw in keywords_list])
    # Filter rows that contain any of the keywords
    # .copy() ensures filtered_df is a new DataFrame, avoiding SettingWithCopyWarning
    filtered_df = temp_df[temp_df['TEMP_FULL_NARRATIVE_FOR_SEARCH'].str.contains(pattern, case=False, na=False)].copy()

    if filtered_df.empty:
        return []

    # Calculate CDESCR length for sorting (on the filtered copy)
    # Ensure CDESCR is string type before applying .str.len()
    filtered_df['CDESCR_LEN'] = filtered_df['CDESCR'].astype(str).str.len()
    
    # Get top N exemplars by CDESCR length
    # Ensure CMPLID is treated as string for output consistency
    top_exemplars_df = filtered_df.nlargest(num_exemplars, 'CDESCR_LEN')

    exemplar_strings_list = []
    for _, row in top_exemplars_df.iterrows():
        # Use the combined narrative for trimming, but ensure it's from original COMPDESC + CDESCR
        # The prompt asks for COMPDESC + CDESCR to be trimmed.
        original_combined_narrative = combine_narratives(row) # Uses original row data
        
        trimmed_narrative = (original_combined_narrative[:247] + "...") if len(original_combined_narrative) > 250 else original_combined_narrative
        
        # Ensure all parts of the exemplar string are strings
        cmplid_str = str(row['CMPLID'])
        yeartxt_str = str(row['YEARTXT'])
        maketxt_str = str(row['MAKETXT'])
        modeltxt_str = str(row['MODELTXT'])
        
        exemplar_strings_list.append(
            f"{cmplid_str}, {yeartxt_str}, {maketxt_str}, {modeltxt_str}: \"{trimmed_narrative}\""
        )
    return exemplar_strings_list

def try_parse_date_for_sorting(date_string):
    """
    Attempts to parse a date string into a datetime object for sorting.
    Returns datetime object or None. This is for internal sorting logic only.
    The original date string is what gets reported.
    """
    if not isinstance(date_string, str):
        return None # Can't parse non-string

    # Handle YYYY or YY (interpreted as 20YY or 19YY)
    if re.fullmatch(r'\b\d{4}\b', date_string):
        try: return datetime(int(date_string), 1, 1)
        except ValueError: return None
    if re.fullmatch(r'\b\d{2}\b', date_string):
        try:
            year = int(date_string)
            year += 2000 if year < 70 else 1900 # Common heuristic for 2-digit years
            return datetime(year, 1, 1)
        except ValueError: return None

    # Extended list of formats to try
    formats_to_try = [
        "%m/%d/%Y", "%m-%d-%Y", "%m/%d/%y", "%m-%d-%y",
        "%Y/%m/%d", "%Y-%m-%d",
        "%B %d, %Y", "%b %d, %Y", "%B %d %Y", "%b %d %Y",
        "%d %B %Y", "%d %b %Y", "%d-%b-%Y", "%d-%B-%Y",
        "%B %Y", "%b %Y", # Month Year
        "%Y%m%d" # YYYYMMDD
    ]
    
    # Normalize potential "Sept" to "Sep" for strptime, and other common short forms
    date_string_normalized = date_string.strip().replace("Sept.", "Sep").replace("Sept", "Sep")
    date_string_normalized = date_string_normalized.replace("Novem.", "Nov").replace("Decem.", "Dec")
    date_string_normalized = date_string_normalized.replace("Octo.", "Oct")


    for fmt in formats_to_try:
        try:
            return datetime.strptime(date_string_normalized, fmt)
        except ValueError:
            continue
    
    return None


def get_knowledge_timeline(df, keywords_list):
    """
    Extracts all literal text dates from narratives (COMPDESC, CDESCR) mentioning keywords.
    Identifies the apparent earliest and latest among these *original string* dates.
    """
    if df.empty or not keywords_list:
        return "No relevant complaints found to extract dates.", "N/A", "N/A"

    # Ensure NARRATIVE_COLUMNS exist
    valid_narrative_cols = [col for col in NARRATIVE_COLUMNS if col in df.columns]
    if not valid_narrative_cols:
        print("Warning: Narrative columns not found for timeline generation.")
        return "Narrative columns not found.", "N/A", "N/A"

    # Create a temporary DataFrame copy for safe operations
    temp_df = df.copy()
    temp_df['TEMP_FULL_NARRATIVE_FOR_SEARCH'] = temp_df.apply(combine_narratives, axis=1)
    
    pattern = '|'.join([re.escape(kw) for kw in keywords_list])
    # Filter to rows containing keywords
    filtered_df = temp_df[temp_df['TEMP_FULL_NARRATIVE_FOR_SEARCH'].str.contains(pattern, case=False, na=False)]

    if filtered_df.empty:
        return "No complaints mentioning the keywords found to extract dates from.", "N/A", "N/A"

    all_date_strings_found = []
    for narrative_text in filtered_df['TEMP_FULL_NARRATIVE_FOR_SEARCH']:
        # Find all occurrences of the date pattern in the narrative
        if pd.notna(narrative_text): # Ensure text is not NaN
            found_dates_in_narrative = re.findall(DATE_REGEX, str(narrative_text), re.IGNORECASE)
            all_date_strings_found.extend([date_str.strip() for date_str in found_dates_in_narrative if date_str.strip()]) # Add non-empty, stripped dates
    
    # Get unique date strings
    unique_date_strings = sorted(list(set(all_date_strings_found)))

    if not unique_date_strings:
        return "No date-like strings found in the narratives of relevant complaints.", "N/A", "N/A"

    # Attempt to determine earliest and latest by parsing for sorting purposes only
    # The original string versions are reported.
    parsed_dates_for_sorting = []
    for s_date in unique_date_strings:
        dt_obj = try_parse_date_for_sorting(s_date)
        if dt_obj:
            # Store both original string and its parsed datetime for sorting
            parsed_dates_for_sorting.append({'original_str': s_date, 'parsed_dt': dt_obj})
    
    earliest_reported_str = "Not determinable from found strings"
    latest_reported_str = "Not determinable from found strings"

    if parsed_dates_for_sorting:
        # Sort by the parsed datetime object
        parsed_dates_for_sorting.sort(key=lambda x: x['parsed_dt'])
        earliest_reported_str = parsed_dates_for_sorting[0]['original_str']
        latest_reported_str = parsed_dates_for_sorting[-1]['original_str']
        
    # Prepare the list of unique date strings for the report
    if len(unique_date_strings) > 15: # Show a sample if too many
        date_list_for_report = ", ".join(unique_date_strings[:15]) + f"... (and {len(unique_date_strings)-15} more unique strings)"
    else:
        date_list_for_report = ", ".join(unique_date_strings) if unique_date_strings else "None found"

    report_text_intro = f"Literal date-like strings found in relevant narratives: {date_list_for_report}. "
    report_text_intro += "No attempt was made to convert or validate these strings beyond a best-effort interpretation for chronological sorting of the unique strings found."
    
    return report_text_intro, earliest_reported_str, latest_reported_str

# --- Main Script Logic ---
def generate_report(df_complaints):
    """Generates the full markdown report."""
    if df_complaints.empty:
        return "Could not generate report: DataFrame is empty or data loading failed."

    report_parts = []

    # --- Preamble ---
    report_parts.append(f"This report analyzes the provided `jaguar_complaints.csv` dataset to identify trends and patterns relevant to recurring automotive issues. The analysis pays particular attention to electrical and cooling systems, aiming to provide context that may be relevant to matters such as California ACP Case {ACP_CASE_REFERENCE} concerning a {ACP_VEHICLE_MODEL_YEAR}, which involves {ACP_KEY_ISSUES} and considerations of {ACP_MMWA_RELEVANCE}.")
    report_parts.append("\n---\n")


    # --- Section 1: Data Corpus & Methodology ---
    report_parts.append("## 1. Data Corpus & Methodology")
    report_parts.append(f"* **File Shape:** The dataframe `df_complaints` (derived from `jaguar_complaints.csv`) has a shape of {df_complaints.shape[0]} rows and {df_complaints.shape[1]} columns.")
    report_parts.append("* **Data Integrity:** Data is loaded directly from the CSV. No parsing beyond standard CSV delimitation is performed by this script, other than ensuring key text fields are treated as strings. No row-level exclusions have been applied to the dataset by this script; every record from the provided CSV file is considered.")
    # Narrative mining columns as per original prompt for this section.
    # The script actually uses COMPDESC, CDESCR for keyword search, but MFR_NAME, MODELTXT are used for other report parts.
    narrative_cols_for_methodology_statement = ['COMPDESC', 'CDESCR', 'MFR_NAME', 'MODELTXT']
    report_parts.append(f"* **Narrative Mining Columns (Primary):** The columns primarily inspected for narrative content for keyword searches are COMPDESC and CDESCR. Columns such as MFR_NAME, MAKETXT, MODELTXT, YEARTXT, and CMPLID are used for identification and grouping as specified.")
    report_parts.append("* **Data Handling:** All records are maintained as loaded from the source file for the purpose of this analysis. Operations are limited to reading specified fields. No records are deleted or sorted in the original dataframe by this script, nor are data types globally cast (beyond initial string conversion for key fields) or dates re-formatted in the original dataframe.")
    report_parts.append("\n")

    # --- Section 2: Quantitative Signals ---
    report_parts.append("## 2. Quantitative Signals (raw counts only)")
    
    # JLR Filter for Make/Model Tally: Uses MFR_NAME as per prompt.
    # The prompt asks for MFR_NAME containing "Jaguar" or "Land Rover".
    # Then, for these, tally by MAKETXT, MODELTXT.
    if 'MFR_NAME' not in df_complaints.columns:
        report_parts.append("* Could not perform JLR Manufacturer Name specific analysis: MFR_NAME column missing.")
        df_jlr_mfr_name_filtered = pd.DataFrame()
    else:
        # Ensure MFR_NAME is string for filtering
        mfr_name_pattern = '|'.join([re.escape(name) for name in JLR_MFR_NAMES])
        df_jlr_mfr_name_filtered = df_complaints[df_complaints['MFR_NAME'].astype(str).str.contains(mfr_name_pattern, case=False, na=False)]

    if not df_jlr_mfr_name_filtered.empty:
        # Tally by MAKETXT, MODELTXT for the MFR_NAME filtered data.
        if 'MAKETXT' in df_jlr_mfr_name_filtered.columns and 'MODELTXT' in df_jlr_mfr_name_filtered.columns:
            # Further filter by specific make names if needed for precision, though MFR_NAME should be sufficient.
            # For this report, VEHICLE_MAKES_FOR_REPORT is used to ensure we only list makes of interest.
            # This step is to align with the prompt's intent of focusing on "Jaguar" or "Land Rover" makes.
            make_pattern_for_tally = '|'.join([re.escape(make) for make in VEHICLE_MAKES_FOR_REPORT])
            
            # Filter on MAKETXT before grouping
            df_for_make_model_tally = df_jlr_mfr_name_filtered[
                df_jlr_mfr_name_filtered['MAKETXT'].astype(str).str.contains(make_pattern_for_tally, case=False, na=False)
            ]

            if not df_for_make_model_tally.empty:
                make_model_counts = df_for_make_model_tally.groupby(
                    [df_for_make_model_tally['MAKETXT'].astype(str), df_for_make_model_tally['MODELTXT'].astype(str)]
                ).size().sort_values(ascending=False) # Sort for readability
                report_parts.append("* **Complaints per Make/Model (where MFR_NAME includes 'Jaguar' or 'Land Rover' and MAKETXT matches):**")
                if not make_model_counts.empty:
                    for (make, model), count in make_model_counts.items():
                        report_parts.append(f"    * {make} {model}: {count} complaints")
                else:
                    report_parts.append("    * No complaints found for specified Jaguar/Land Rover makes/models after MFR_NAME and MAKETXT filtering.")
            else:
                report_parts.append("    * No complaints found matching MAKETXT 'Jaguar' or 'Land Rover' after MFR_NAME filtering.")
        else:
            report_parts.append("* MAKETXT or MODELTXT column missing from MFR_NAME filtered data, cannot provide make/model breakdown.")
    else:
        report_parts.append("* No complaints found matching MFR_NAME 'Jaguar' or 'Land Rover' in the dataset.")

    electrical_keywords_count = count_keyword_mentions(df_complaints, ELECTRICAL_KEYWORDS)
    cooling_keywords_count = count_keyword_mentions(df_complaints, COOLING_KEYWORDS)
    report_parts.append(f"* **Electrical Keyword Mentions (Dataset-wide):** {electrical_keywords_count} rows mention one or more electrical keywords (e.g., {', '.join(ELECTRICAL_KEYWORDS[:3])}...).")
    report_parts.append(f"* **Cooling Keyword Mentions (Dataset-wide):** {cooling_keywords_count} rows mention one or more cooling keywords (e.g., {', '.join(COOLING_KEYWORDS[:3])}...).")
    report_parts.append("\n")

    # --- Section 3: Qualitative Exemplars ---
    report_parts.append("## 3. Qualitative Exemplars (longest CDESCR, Dataset-wide)")
    report_parts.append("* **Electrical Keyword Exemplars:**")
    electrical_exemplars = get_narrative_exemplars(df_complaints, ELECTRICAL_KEYWORDS)
    if electrical_exemplars:
        for ex in electrical_exemplars: report_parts.append(f"    * {ex}")
    else:
        report_parts.append("    * No complaints found matching electrical keywords for exemplars.")

    report_parts.append("* **Cooling Keyword Exemplars:**")
    cooling_exemplars = get_narrative_exemplars(df_complaints, COOLING_KEYWORDS)
    if cooling_exemplars:
        for ex in cooling_exemplars: report_parts.append(f"    * {ex}")
    else:
        report_parts.append("    * No complaints found matching cooling keywords for exemplars.")
    report_parts.append("\n")
    
    # --- Section 4: Manufacturer Knowledge Timeline ---
    report_parts.append("## 4. Manufacturer Knowledge Timeline (Dataset-wide)")
    report_parts.append("* **Electrical Keywords:**")
    el_dates_text, el_earliest, el_latest = get_knowledge_timeline(df_complaints, ELECTRICAL_KEYWORDS)
    report_parts.append(f"    * {el_dates_text}")
    report_parts.append(f"    * Apparent earliest literal text date found: `{el_earliest}`")
    report_parts.append(f"    * Apparent latest literal text date found: `{el_latest}`")

    report_parts.append("* **Cooling Keywords:**")
    cl_dates_text, cl_earliest, cl_latest = get_knowledge_timeline(df_complaints, COOLING_KEYWORDS)
    report_parts.append(f"    * {cl_dates_text}")
    report_parts.append(f"    * Apparent earliest literal text date found: `{cl_earliest}`")
    report_parts.append(f"    * Apparent latest literal text date found: `{cl_latest}`")
    report_parts.append("\n")

    # --- Section 5: Implications for ACP Review (Contextualized) ---
    report_parts.append("## 5. Implications for ACP Review")
    report_parts.append(f"The following implications are drawn from the dataset-wide analysis and may offer context for reviewing specific cases like {ACP_CASE_REFERENCE} involving a {ACP_VEHICLE_MODEL_YEAR}:")

    insight1 = (f"1. The {electrical_keywords_count} dataset-wide complaints related to electrical systems, with issues such as "
                f"'{ELECTRICAL_KEYWORDS[0]}' and '{ELECTRICAL_KEYWORDS[1]}' (e.g., CMPLID `{electrical_exemplars[0].split(',')[0] if electrical_exemplars else 'N/A'}`), "
                f"may indicate broader patterns of electrical component reliability. Such patterns could be relevant when assessing whether similar issues in specific vehicles, "
                f"like the {ACP_VEHICLE_MODEL_YEAR}, represent isolated incidents or part of a wider trend potentially engaging MMWA protections if not adequately resolved under warranty.")
    report_parts.append(insight1)

    insight2 = (f"2. The {cooling_keywords_count} dataset-wide complaints concerning cooling systems, mentioning terms like "
                f"'{COOLING_KEYWORDS[0]}' (e.g., CMPLID `{cooling_exemplars[0].split(',')[0] if cooling_exemplars else 'N/A'}`), "
                f"could suggest recurring concerns. If such issues lead to multiple repair attempts or unresolved problems, as alleged in some consumer complaints, "
                f"this may bear on MMWA's 'reasonable number of attempts' provision, particularly for vehicles like the {ACP_VEHICLE_MODEL_YEAR} experiencing similar defects.")
    report_parts.append(insight2)

    insight3 = (f"3. The identification of literal date mentions in narratives, with electrical issues noted from as early as `{el_earliest}` "
                f"and cooling issues from `{cl_earliest}` across the dataset, could be cross-referenced with manufacturer service bulletins or internal knowledge timelines. "
                f"This might help ascertain when JLR potentially became aware of certain component vulnerabilities, a factor that can be relevant in evaluating warranty and MMWA claims for specific cases like {ACP_CASE_REFERENCE}.")
    report_parts.append(insight3)
    report_parts.append("\n")

    # --- Section 6: Forward‑Looking Questions (Contextualized) ---
    report_parts.append("## 6. Forward-Looking Questions")
    report_parts.append(f"The following questions are based on the dataset analysis and are posed to potentially assist the ACP in its review of matters like {ACP_CASE_REFERENCE}:")

    q1 = (f"1. Given the {electrical_keywords_count} electrical complaints identified dataset-wide, including issues like 'short to ground' or 'door module' failures, "
          f"what data can JLR provide regarding the prevalence, diagnostic challenges, and repair efficacy for similar electrical components in {ACP_VEHICLE_MODEL_YEAR}s and related platforms? "
          f"How do repeated repair attempts for such issues align with JLR's obligations under its written warranty and the MMWA?")
    report_parts.append(q1)

    q2 = (f"2. In light of {cooling_keywords_count} cooling system complaints (e.g., 'coolant leaks', 'expansion tank issues'), what percentage of these issues for Jaguar/Land Rover vehicles, "
          f"and specifically for models like the {ACP_VEHICLE_MODEL_YEAR}, typically require multiple dealer visits or part replacements? "
          f"What is JLR's definition of a 'reasonable number of attempts' or 'reasonable time' for resolving such critical system failures under warranty and MMWA?")
    report_parts.append(q2)
    
    q3 = (f"3. Considering that JLR's referral for case {ACP_CASE_REFERENCE} reportedly required use of BBB AUTO LINE before MMWA court action, and that BBB AUTO LINE's rules may reference FTC regulations (16 C.F.R. Part 703 implementing MMWA), "
          f"how does BBB AUTO LINE reconcile decisions to decline jurisdiction over MMWA-relevant claims for used vehicles (not meeting Song-Beverly 'new vehicle' definitions) with the explicit MMWA pre-dispute resolution requirement stated by the manufacturer and the program's potential scope under federal law?")
    report_parts.append(q3)

    return "\n".join(report_parts)

if __name__ == "__main__":
    # --- IMPORTANT: SET THE PATH TO YOUR CSV FILE HERE ---
    # Option 1: Place 'jaguar_complaints.csv' in the same directory as this script.
    # csv_file_path = "jaguar_complaints.csv" 
    
    # Option 2: Provide the full path to the CSV file.
    # Example for Windows: csv_file_path = r"C:\Users\YourUser\Documents\jaguar_complaints.csv"
    # Example for macOS/Linux: csv_file_path = "/Users/YourUser/Documents/jaguar_complaints.csv"
    # For the execution environment, it's often in a specific working directory.
    # Let's assume it's in the current working directory for simplicity here.
    csv_file_path = "/content/jaguar_complaints.csv" # MODIFY AS NEEDED

    print(f"Script execution started. Current working directory: {os.getcwd()}")
    
    df_complaints_loaded = load_data(csv_file_path)
    
    if not df_complaints_loaded.empty:
        print("Data loaded successfully. Generating report...")
        markdown_report = generate_report(df_complaints_loaded)
        print("\n--- REPORT START ---")
        print(markdown_report)
        print("--- REPORT END ---\n")
        
        # Optionally, save the report to a file
        try:
            with open("jlr_complaints_analysis_report.md", "w", encoding="utf-8") as f:
                f.write(markdown_report)
            print(f"Report successfully saved to: {os.path.abspath('jlr_complaints_analysis_report.md')}")
        except Exception as e:
            print(f"Error saving report to file: {e}")
            
    else:
        print("Script terminated: Data loading failed or DataFrame is empty. No report generated.")

