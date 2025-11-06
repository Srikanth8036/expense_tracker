import os
import pandas as pd
from utils.logger import logs

class Csv_data_analyzer:
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DATA_DIR = os.path.join(BASE_DIR, "data")
    CSV_PATH = os.path.join(DATA_DIR, "sales.csv")

    def list_csv_files(self):
        """Return only .csv files in data dir."""
        if not os.path.isdir(self.DATA_DIR):
            raise FileNotFoundError(f"Data folder missing: {self.DATA_DIR}")
        files = [f for f in os.listdir(self.DATA_DIR) if f.lower().endswith(".csv")]
        if not files:
            raise FileNotFoundError(f"No CSVs found in {self.DATA_DIR}")
        return sorted(files)

    def export_csv(self, input_csv_path, df):
        """Write df next to input file as <name>_exported.csv and return the path."""
        if not os.path.exists(input_csv_path):
            logs.error("file not found error")
            raise FileNotFoundError(f"{input_csv_path} no such file found")

        base = os.path.splitext(os.path.basename(input_csv_path))[0]
        out_csv = os.path.join(self.DATA_DIR, f"{base}_exported.csv")
        df.to_csv(out_csv, index=False)
        logs.info(f"data exported successfully: {out_csv}")
        print(f"Exported: {out_csv}")
        return out_csv

    def generate_summary(self, df, column_name):
        """Return a summary DataFrame for a numeric column. Raises on bad column."""
        if column_name not in df.columns:
            msg = f"Column '{column_name}' not found in CSV"
            logs.error(msg)
            raise KeyError(msg)

        # Coerce to numeric; drop non-numeric rows
        series = pd.to_numeric(df[column_name], errors="coerce")
        if series.notna().sum() == 0:
            msg = f"Column '{column_name}' has no numeric values"
            logs.error(msg)
            raise ValueError(msg)

        summary = {
            "Metric": [
                "Column",
                "Sum",
                "Avg",
                "Min",
                "Max",
                "Count",
                "Non-NaN Count",
            ],
            "Value": [
                column_name,
                series.sum(),
                series.mean(),
                series.min(),
                series.max(),
                series.size,        # original size (including NaNs)
                series.notna().sum()
            ],
        }
        summary_df = pd.DataFrame(summary)
        logs.info("summary generated successfully")
        return summary_df
