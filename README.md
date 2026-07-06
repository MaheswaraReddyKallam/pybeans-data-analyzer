# PyBeans Data Analyzer & CLI 📊☕

### Overview
A command-line interface (CLI) application built to process, clean, and analyze retail sales data for a fictional coffee shop (PyBeans). The script transforms raw, messy data into actionable business intelligence using Pandas, wrapped in an interactive menu for non-technical users.

### Technologies Used
* **Python** (Control flow, standard library)
* **Pandas** (DataFrames, boolean filtering, aggregation)

### Key Features
* **Data Cleaning:** Automatically filters out closed-store days (zero-value rows) prior to analysis to prevent skewed averages.
* **Feature Engineering:** Programmatically generates a `Total_Revenue` column by calculating units sold against price-per-unit.
* **Data Aggregation:** Utilizes `.groupby()` mechanics to calculate revenue strictly by item categories.
* **Interactive CLI:** Features a continuous `while` loop menu, allowing end-users to query specific datasets on demand without interacting with the codebase.

### How to Run
1. Ensure Pandas is installed: `pip install pandas`
2. Run the script in your terminal: `python analyzer.py`
3. Follow the on-screen menu prompts to explore the data.
