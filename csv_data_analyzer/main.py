from utils.file_utils import Csv_data_analyzer
from utils.logger import logs
import os
import pandas as pd

class Main_class:
    def __init__(self):
        self.folder_path = Csv_data_analyzer.DATA_DIR

    def show_files(self, files):
        print("\nAvailable CSV files:")
        for idx, f in enumerate(files, 1):
            print(f"  {idx}. {f}")

    def choose_index(self, prompt, max_index):
        """Prompt until a valid 1..max_index int is entered, or return None to exit."""
        attempts = 3
        while attempts > 0:
            raw = input(prompt).strip()
            if raw.lower() in {"q", "quit", "exit"}:
                return None
            try:
                val = int(raw)
                if 1 <= val <= max_index:
                    return val
                print(f"Enter a number between 1 and {max_index}.")
            except ValueError:
                print("Invalid input, enter a number.")
            attempts -= 1
        return None

    def main(self, obj: Csv_data_analyzer):
        # menu
        choice = None
        attempts = 3
        while attempts > 0:
            raw = input("\npress 1 for View Summary\npress 2 for Export to CSV\npress 3 for Exit\n> ").strip()
            try:
                choice = int(raw)
                if choice in (1, 2, 3):
                    break
                print("Only 1, 2, 3 allowed.")
            except ValueError:
                print("Invalid input, enter 1/2/3.")
            attempts -= 1

        if choice is None or choice == 3:
            logs.info("user chose exit")
            print("thank you see you again........")
            return

        # list csvs
        try:
            files = obj.list_csv_files()
        except Exception as e:
            logs.error(f"Failed to list CSVs: {e}")
            print(f"Error: {e}")
            return

        self.show_files(files)
        idx = self.choose_index("Select a CSV by number (or 'q' to cancel): ", len(files))
        if idx is None:
            print("Cancelled.")
            return

        filename = files[idx - 1]
        csv_path = os.path.join(self.folder_path, filename)

        if choice == 1:
            # summary flow
            try:
                df = pd.read_csv(csv_path)
                logs.info(f"csv loaded for summary: {csv_path}")
            except Exception as e:
                logs.error(f"Failed to read CSV: {e}")
                print(f"Error reading CSV: {e}")
                return

            print("\nColumns:")
            for i, col in enumerate(df.columns, 1):
                print(f"  {i}. {col}")
            col_idx = self.choose_index("Pick a column number for summary: ", len(df.columns))
            if col_idx is None:
                print("Cancelled.")
                return
            column_name = df.columns[col_idx - 1]

            try:
                summary_df = obj.generate_summary(df, column_name)
                print("\nSummary:")
                print(summary_df.to_string(index=False))
            except Exception as e:
                logs.error(f"Summary failed: {e}")
                print(f"Error: {e}")

        elif choice == 2:
            # export flow
            try:
                df = pd.read_csv(csv_path)
                logs.info(f"csv loaded for export: {csv_path}")
            except Exception as e:
                logs.error(f"Failed to read CSV: {e}")
                print(f"Error reading CSV: {e}")
                return

            try:
                out_path = obj.export_csv(csv_path, df)
                print(f"Exported to: {out_path}")
            except Exception as e:
                logs.error(f"Export failed: {e}")
                print(f"Export error: {e}")

if __name__ == '__main__':
    logs.info('main fun is called........')
    print('this is main calling')
    csv_analyser = Csv_data_analyzer()
    Main_class().main(csv_analyser)
