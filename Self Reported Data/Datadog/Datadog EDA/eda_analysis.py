#!/usr/bin/env python3
"""
Exploratory Data Analysis for Jaguar F-Type Vehicle Telemetry Data
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import glob
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# Set style for plots
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

class JaguarTelemetryEDA:
    def __init__(self, data_dir):
        self.data_dir = Path(data_dir)
        self.dataframes = {}
        self.combined_df = None
        self.column_info = {}

    def load_all_files(self):
        """Load all CSV files and examine their structure"""
        csv_files = glob.glob(str(self.data_dir / "*.csv"))

        for file_path in csv_files:
            file_name = Path(file_path).name
            print(f"Loading {file_name}...")

            # Try different encodings
            encodings = ['utf-8', 'utf-16', 'latin1', 'cp1252']
            df = None

            for encoding in encodings:
                try:
                    # Read first few lines to understand structure
                    with open(file_path, 'r', encoding=encoding) as f:
                        lines = f.readlines()

                    # Skip header lines and read CSV data
                    data_start_line = 0
                    for i, line in enumerate(lines):
                        if 'Time(s)' in line:
                            data_start_line = i
                            break

                    # Read the actual data
                    df = pd.read_csv(file_path, skiprows=data_start_line, encoding=encoding)
                    print(f"  Successfully loaded with {encoding} encoding")
                    break
                except UnicodeDecodeError:
                    continue
                except Exception as e:
                    print(f"  Error with {encoding}: {e}")
                    continue

            if df is None:
                print(f"  Failed to load {file_name} with any encoding")
                continue

            # Clean column names
            df.columns = df.columns.str.strip()

            # Convert time to numeric if it's not already
            if 'Time(s)' in df.columns:
                df['Time(s)'] = pd.to_numeric(df['Time(s)'], errors='coerce')

            # Store dataframe
            self.dataframes[file_name] = df

            # Store column information
            self.column_info[file_name] = {
                'columns': list(df.columns),
                'n_rows': len(df),
                'n_cols': len(df.columns)
            }

        print(f"Loaded {len(self.dataframes)} files successfully.")

    def get_dataset_overview(self):
        """Provide overview of the dataset"""
        print("\n" + "="*60)
        print("DATASET OVERVIEW")
        print("="*60)

        total_rows = sum(info['n_rows'] for info in self.column_info.values())
        all_columns = set()
        for info in self.column_info.values():
            all_columns.update(info['columns'])

        print(f"Total files: {len(self.dataframes)}")
        print(f"Total observations: {total_rows}")
        print(f"Unique variables: {len(all_columns)}")

        # File details
        print("\nFile Details:")
        for file_name, info in self.column_info.items():
            date_str = file_name.replace('DataLog-', '').replace('.csv', '').replace('_', ' ')
            print(f"  {file_name}: {info['n_rows']} rows, {info['n_cols']} columns")
            print(f"    Variables: {', '.join(info['columns'][:5])}{'...' if len(info['columns']) > 5 else ''}")

    def analyze_missing_data(self):
        """Analyze missing data patterns"""
        print("\n" + "="*60)
        print("MISSING DATA ANALYSIS")
        print("="*60)

        for file_name, df in self.dataframes.items():
            print(f"\n{file_name}:")
            missing_counts = df.isnull().sum()
            missing_percentages = (missing_counts / len(df)) * 100

            missing_info = pd.DataFrame({
                'Missing Count': missing_counts,
                'Missing Percentage': missing_percentages
            })

            # Only show columns with missing data
            missing_info = missing_info[missing_info['Missing Count'] > 0]

            if not missing_info.empty:
                print(missing_info.round(2))
            else:
                print("  No missing data")

    def get_summary_statistics(self):
        """Generate summary statistics for numeric variables"""
        print("\n" + "="*60)
        print("SUMMARY STATISTICS")
        print("="*60)

        # Combine all dataframes for analysis
        all_data = []
        for file_name, df in self.dataframes.items():
            # Add source file info
            temp_df = df.copy()
            # Convert columns to numeric where possible
            for col in temp_df.columns:
                if col != 'source_file':
                    temp_df[col] = pd.to_numeric(temp_df[col], errors='coerce')
            temp_df['source_file'] = file_name
            all_data.append(temp_df)

        if all_data:
            self.combined_df = pd.concat(all_data, ignore_index=True, sort=False)

            # Get numeric columns
            numeric_cols = self.combined_df.select_dtypes(include=[np.number]).columns
            numeric_cols = [col for col in numeric_cols if col != 'source_file']

            if numeric_cols:
                summary_stats = self.combined_df[numeric_cols].describe()
                print("Numeric Variables Summary:")
                print(summary_stats.round(2))

                # Additional statistics
                print("\nAdditional Statistics:")
                for col in numeric_cols[:5]:  # Limit to first 5 to avoid too much output
                    if col in self.combined_df.columns:
                        data = self.combined_df[col].dropna()
                        if len(data) > 0:
                            print(f"\n{col}:")
                            print(f"  Skewness: {data.skew():.3f}")
                            print(f"  Kurtosis: {data.kurtosis():.3f}")
                            if data.std() > 0:
                                print(f"  Coefficient of variation: {(data.std()/data.mean()):.3f}")

    def analyze_correlations(self):
        """Analyze correlations between variables"""
        print("\n" + "="*60)
        print("CORRELATION ANALYSIS")
        print("="*60)

        if self.combined_df is not None:
            # Convert potentially numeric string columns to numeric
            df_numeric = self.combined_df.copy()
            for col in df_numeric.columns:
                if col not in ['source_file', 'Time(s)']:
                    df_numeric[col] = pd.to_numeric(df_numeric[col], errors='coerce')

            # Get numeric columns
            numeric_cols = df_numeric.select_dtypes(include=[np.number]).columns
            numeric_cols = [col for col in numeric_cols if col not in ['source_file', 'Time(s)']]

            if len(numeric_cols) > 1:
                # Calculate correlation matrix
                corr_matrix = df_numeric[numeric_cols].corr()

                # Display strong correlations
                print("Strong correlations (|r| > 0.7):")
                strong_corr = []
                for i in range(len(corr_matrix.columns)):
                    for j in range(i+1, len(corr_matrix.columns)):
                        corr_val = corr_matrix.iloc[i, j]
                        if abs(corr_val) > 0.7 and not np.isnan(corr_val):
                            strong_corr.append({
                                'var1': corr_matrix.columns[i],
                                'var2': corr_matrix.columns[j],
                                'correlation': corr_val
                            })

                if strong_corr:
                    for corr in sorted(strong_corr, key=lambda x: abs(x['correlation']), reverse=True):
                        print(".3f")
                else:
                    print("No strong correlations found.")
            else:
                print("Insufficient numeric variables for correlation analysis.")

    def create_visualizations(self):
        """Create key visualizations"""
        if self.combined_df is None:
            return

        # Create output directory for plots
        plots_dir = self.data_dir / "plots"
        plots_dir.mkdir(exist_ok=True)

        # Distribution plots for key variables
        key_vars = ['Engine RPM (rpm)', 'Vehicle Speed (MPH)', 'Engine Coolant Temperature (°F)',
                   'Fuel Rail Pressure (PSI)', 'Mass Air Flow Rate (lb/min)']

        fig, axes = plt.subplots(2, 3, figsize=(15, 10))
        axes = axes.ravel()

        for i, var in enumerate(key_vars):
            if var in self.combined_df.columns and i < len(axes):
                data = self.combined_df[var].dropna()
                if len(data) > 0:
                    sns.histplot(data=data, ax=axes[i], bins=50)
                    axes[i].set_title(f'Distribution of {var}')
                    axes[i].set_xlabel(var)

        if len(key_vars) < len(axes):
            axes[len(key_vars)].axis('off')

        plt.tight_layout()
        plt.savefig(plots_dir / 'distributions.png', dpi=300, bbox_inches='tight')
        plt.close()

        # Correlation heatmap
        numeric_cols = self.combined_df.select_dtypes(include=[np.number]).columns
        numeric_cols = [col for col in numeric_cols if col not in ['source_file', 'Time(s)']]

        if len(numeric_cols) > 1:
            plt.figure(figsize=(12, 10))
            corr_matrix = self.combined_df[numeric_cols].corr()
            mask = np.triu(np.ones_like(corr_matrix, dtype=bool))
            sns.heatmap(corr_matrix, mask=mask, annot=False, cmap='coolwarm', center=0,
                       square=True, linewidths=.5, cbar_kws={"shrink": .5})
            plt.title('Correlation Heatmap of Vehicle Sensors')
            plt.xticks(rotation=45, ha='right')
            plt.yticks(rotation=0)
            plt.tight_layout()
            plt.savefig(plots_dir / 'correlation_heatmap.png', dpi=300, bbox_inches='tight')
            plt.close()

        print(f"\nVisualizations saved to {plots_dir}")

    def analyze_time_series_patterns(self):
        """Analyze time series patterns in the data"""
        print("\n" + "="*60)
        print("TIME SERIES ANALYSIS")
        print("="*60)

        for file_name, df in self.dataframes.items():
            if 'Time(s)' in df.columns and len(df) > 10:
                print(f"\n{file_name}:")
                print(f"  Duration: {df['Time(s)'].max():.1f} seconds")
                print(f"  Sampling rate: ~{len(df)/df['Time(s)'].max():.2f} Hz")

                # Check for key variables
                key_vars = ['Engine RPM (rpm)', 'Vehicle Speed (MPH)', 'Engine Coolant Temperature (°F)']
                for var in key_vars:
                    if var in df.columns:
                        data = pd.to_numeric(df[var], errors='coerce').dropna()
                        if len(data) > 0:
                            print(f"  {var}: range [{data.min():.1f}, {data.max():.1f}]")

    def run_full_analysis(self):
        """Run complete EDA analysis"""
        print("Starting Jaguar F-Type Telemetry Data Analysis")
        print("="*60)

        self.load_all_files()
        self.get_dataset_overview()
        self.analyze_missing_data()
        self.get_summary_statistics()
        self.analyze_correlations()
        self.analyze_time_series_patterns()
        self.create_visualizations()

        print("\n" + "="*60)
        print("ANALYSIS COMPLETE")
        print("="*60)

if __name__ == "__main__":
    # Run the analysis
    data_dir = "/Users/ree/Downloads/Jaguar F-Type/Datadog"
    eda = JaguarTelemetryEDA(data_dir)
    eda.run_full_analysis()
