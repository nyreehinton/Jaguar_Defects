# The Goal: From Snippets to Stories

Instead of extracting just the most representative sentence for a key issue, we will now identify and extract the **entire summary** from which that sentence came. This summary will be the single best exemplar of a specific, distinctive issue for that vehicle model.

### The Methodology: How to Find the "Best" Summary

We will adapt the existing logic. The principle remains the same: for a given high-lift (distinctive) term, we want the most representative text.

1.  **Identify Top Distinctive Terms**: We still use **lift** to find the terms that uniquely characterize a model's issues (e.g., "joystick", "delamination", "stall").
2.  **Gather Candidate Sentences**: For each top term, we collect all sentences from all summaries within the model's group that contain that term.
3.  **Find the Centroid Sentence**: We vectorize these sentences using TF-IDF and find the one closest to the vector centroid. This is our "most representative sentence."
4.  **Retrieve the Parent Summary (The Key Change)**: Instead of just stopping at the sentence, we now identify the original document (`id` and `summary`) from which this centroid sentence was extracted.
5.  **Store the Full Summary**: This full, original summary is then saved as the best example for that specific issue.

This approach ensures that the summary we select is not just any random report containing the keyword, but one that discusses the issue in a way that is most typical of all other reports about the same issue.

---

### Code Modifications

I will update two key functions: `analyze_group` to extract the full summary, and `generate_markdown_report` to display it properly.

#### 1. Modification to `analyze_group()`

We need to pass the original summaries into this function and adjust the "Representative Sentences" section.

```python
# In the main() function, change the call to analyze_group:
# ...
# groups = df_analysis.groupby('make_model_year')
# for group_name, group_df in tqdm(groups, desc="Analyzing Vehicle Groups"):
#     # ...
#     group_tokens = group_df[['id', 'lemmas', 'sentences']] # Add 'id' to link back
#     original_summaries = group_df.set_index('id')['summary'] # Pass original summaries
#     profile = analyze_group(group_df, group_tokens, original_summaries, group_name, global_stats, config)
#     # ...

# --- MODIFIED: analyze_group function signature and logic ---
def analyze_group(group_df, group_tokens, original_summaries, group_name, global_stats, config):
    """Performs deep descriptive analysis for a single vehicle group."""
    profile = {"group_name": group_name}
    
    # ... [Sections 1-5: Volume, Time Series, Terms, N-grams, Keyphrases remain the same] ...

    # 6. Representative Summaries (Previously Representative Sentences)
    # For the top 3 most distinctive terms
    top_terms_for_summaries = list(profile.get('top_distinctive_terms', {}).keys())[:3]
    representative_summaries = {}

    # Create a lookup from sentence to its document ID
    sentence_to_id = {}
    for _, row in group_tokens.iterrows():
        for sentence in row['sentences']:
            # Store the first ID found for a unique sentence
            if sentence not in sentence_to_id:
                sentence_to_id[sentence] = row['id']

    for term in top_terms_for_summaries:
        # Find all sentences containing the term
        relevant_sentences = [
            s for sentences_list in group_tokens['sentences'] for s in sentences_list if term in s.lower()
        ]
        
        if len(relevant_sentences) > 1:
            # Vectorize sentences to find centroid
            sent_vectorizer = TfidfVectorizer()
            try:
                sent_vectors = sent_vectorizer.fit_transform(relevant_sentences)
                centroid = sent_vectors.mean(axis=0)
                
                # Find sentence closest to centroid
                similarities = cosine_similarity(sent_vectors, centroid)
                closest_sent_idx = similarities.argmax()
                best_sentence = relevant_sentences[closest_sent_idx]
                
                # Use the best sentence to find the parent document ID
                doc_id = sentence_to_id.get(best_sentence)
                if doc_id:
                    # Retrieve the full original summary
                    full_summary = original_summaries.loc[doc_id]
                    representative_summaries[term] = {
                        "representative_sentence": best_sentence,
                        "full_summary": full_summary
                    }
            except ValueError: # Happens if all words in relevant_sentences are stopwords
                continue

        elif relevant_sentences:
            # If only one sentence, use it
            best_sentence = relevant_sentences[0]
            doc_id = sentence_to_id.get(best_sentence)
            if doc_id:
                full_summary = original_summaries.loc[doc_id]
                representative_summaries[term] = {
                    "representative_sentence": best_sentence,
                    "full_summary": full_summary
                }
            
    profile['representative_summaries'] = representative_summaries

    return profile
```

#### 2. Modification to `generate_markdown_report()`

We'll update the report to show the full summary in a clean, readable format.

```python
# --- MODIFIED: generate_markdown_report function ---
def generate_markdown_report(profiles, outdir, config):
    """Generates a human-friendly markdown executive report."""
    logging.info("Generating markdown executive report...")
    report_path = outdir / "REPORT.md"
    
    # ... [Sorting and report header remain the same] ...

    with open(report_path, 'w') as f:
        # ... [Write headers] ...
        
        for profile in sorted_profiles[:15]:
            # ... [Write group name, volume, etc.] ...
            
            f.write("\n### Representative Complaint Summaries\n\n")
            summaries = profile.get('representative_summaries', {})
            if summaries:
                for term, data in summaries.items():
                    f.write(f"**The most representative summary related to the issue of `{term}`:**\n\n")
                    f.write("> **Original Summary:**\n")
                    # Format the summary as a blockquote
                    formatted_summary = "> " + data['full_summary'].replace('\n', '\n> ')
                    f.write(f"{formatted_summary}\n\n")
            else:
                f.write("- No representative summaries could be extracted for the top issues.\n\n")

            # ... [Rest of the report (Trends, Spikes, etc.) remains the same] ...
```

### What the New Output Looks Like

With these changes, the `REPORT.md` will be much more powerful. For the ALTEC AH SERIES example, the report section would look like this:

---

## Analysis for: ALTEC | AH SERIES | 2023

-   **Total Records:** 150
-   **Top Implicated Components:** UNKNOWN OR OTHER, EQUIPMENT

### Key Issues & Distinctive Language

The following terms and phrases are uniquely prevalent for this model, indicating specific problem areas:

-   **joystick** (Lift: 25.41): This term appears significantly more often for this model compared to others.
-   **single-axis** (Lift: 22.15): Suggests a specific component type is involved.
-   **drift** (Lift: 18.90): Describes a specific failure mode of the control system.

### Representative Complaint Summaries

**The most representative summary related to the issue of `joystick`:**

> **Original Summary:**
> Altec has learned that the single-axis joystick controller for the primary control station may experience a drift condition. This condition can cause the aerial device to move unexpectedly when the controller is released. An investigation determined that a component within the joystick assembly may fail, leading to the drift. The operator reported that the boom started to lower on its own without any input. The unit was immediately taken out of service. Dealer was notified and is awaiting replacement parts.

**The most representative summary related to the issue of `drift`:**

> **Original Summary:**
> Customer states that the main boom control joystick exhibits intermittent drift. After operating for approximately 20 minutes, the joystick will not return to a true neutral position, causing the boom to slowly creep downward. This requires the operator to constantly correct the position. The issue is more pronounced in warmer weather. We have attempted to recalibrate the controller per the service manual, but the drift returns after a short period of use. This appears to be a hardware fault within the joystick itself.

---

This provides immediate, actionable insight. An engineer can read the full description and understand the symptoms, conditions, and operator's experience without having to go back to the source database.