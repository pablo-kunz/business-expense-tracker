Business Expense Tracker 📊

Personal Project — Python Automation
Universidad Tecnológica Nacional (UTN) — Programming Technician Degree

Developed by: Pablo Kunz


Description

Console-based application built in Python that reads business expense data from a CSV file and generates detailed reports. Designed for small businesses that need to track and analyze their operational costs (raw materials, supplies, services, logistics, salaries, etc.).


Project Structure

├── main.py              # Entry point: menu and program flow
├── expenses.py          # Core logic: data processing and analysis
└── expenses_data.csv    # Sample expense dataset


Requirements


Python 3.x (no external libraries required)



How to Run


Clone or download this repository.
Make sure all files are in the same folder.
Run from the terminal:


bashpython3 main.py


Features


Total spent by category — ranked from highest to lowest
Total spent by month — sorted chronologically
Most expensive month
Monthly average spending
Filter expenses by date range
Export full summary report to a new CSV file



Key Concepts Applied


Modular design separating logic (expenses.py) from program flow (main.py)
CSV file reading and writing with the csv module
Date parsing and filtering with the datetime module
Dictionary-based data aggregation
try/except for robust input validation



Example Output

30 expense records loaded successfully.

===== BUSINESS EXPENSE TRACKER =====
1. Total spent by category
2. Total spent by month
3. Most expensive month
4. Monthly average
5. Filter expenses by date range
6. Export summary report to CSV
0. Exit
=====================================

--- TOTAL BY CATEGORY ---
  Salaries: $135,000.00
  Raw Materials: $95,500.00
  Services: $53,000.00
  Logistics: $28,100.00
  Supplies: $14,900.00
  Maintenance: $10,400.00


CSV Format

date,category,amount,description
2026-01-05,Raw Materials,15000,Steel sheets
2026-02-25,Salaries,45000,Monthly payroll
