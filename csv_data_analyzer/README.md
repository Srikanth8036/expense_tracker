# CSV Data Analyzer

A small utility for analyzing CSV files (sales and reports). This project provides helpers to read CSVs, summarize sales data, and export reports. It is lightweight and intended as a learning / mini-project.

## Features
- Load CSV files from the `data/` directory
- Produce simple summaries and reports
- Logs operations to `logs/csv_analyzers.log`

## Requirements
This project requires Python 3.8+ and the following Python packages (listed in `requriments.txt`):

```
pandas
```

Install dependencies with pip (recommended inside a virtualenv):

```powershell
# From the project folder
python -m pip install -r requriments.txt
```

## Project structure

```
csv_data_analyzer/
	main.py                 # entry-point for running the analyzer
	requriments.txt         # project dependencies (pandas)
	data/
		sales.csv
		sales_exported.csv
		reports.csv
	logs/
		csv_analyzers.log     # generated application log
	utils/
		file_utils.py         # CSV read/processing helpers
		logger.py             # logging configuration
```

## How to run

From the `csv_data_analyzer` directory run:

```powershell
# run the analyzer
python main.py
```

The program will use the helper functions in `utils/` to read files from the `data/` folder. Logs will be written to the `logs/` directory.

## Notes
- If you see import errors like `ModuleNotFoundError: No module named 'logger'`, run the script from the `csv_data_analyzer` package folder (so package imports resolve). Alternatively, run Python with the package path set correctly, for example:

```powershell
# from the workspace root
python -m csv_data_analyzer.main
```

## License
This project has no license defined. Add one if you plan to distribute the code.

