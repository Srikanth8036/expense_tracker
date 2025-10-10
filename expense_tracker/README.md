# Expense Tracker CLI Tool

A simple **Command-Line Expense Tracker** built with Python to manage and analyze your daily expenses.  
This tool allows you to **add**, **view**, **search**, and **summarize** your expenses by category and month.  
All data is stored persistently in a local CSV file (`expense.csv`).

---

## Features

- Add expenses with category, description, and amount  
- View all recorded expenses  
- Search expenses by category  
- View total monthly expenses  
- Persistent CSV storage (data saved between runs)  
- Logging for error tracking  

---

## Project Structure
expense_tracker/
│
├── main.py # Entry point for the program
├── expense.csv # Stores all expense records
├── logging.txt # Stores logs
└── README.md # Project documentation


---

## Requirements

Install dependencies using:

```bash
pip install pandas
git clone https://github.com/Srikanth8036/expense_tracker.git
cd expense_tracker
python main.py
==========================
 EXPENSE TRACKER CLI TOOL
==========================

1. Add Expense
2. View All Expenses
3. Search by Category
4. View Monthly Summary
5. Exit

Enter your category: Food
Enter your description: Lunch at Cafe
Enter the amount: 250
Expense added successfully!

Enter your Category ("food", "travel","entertainment")
food

Category  Description      Amount
Food      Lunch at Cafe    250

Total expense for category "food": 250

Enter your month to get the total expense on month(oct,sep,...):- October
monthly: October is total expenses are 1250

| Function               | Description                                  |
| ---------------------- | -------------------------------------------- |
| `add_expense()`        | Adds a new expense and saves it to CSV       |
| `view_expenses()`      | Displays all stored expenses                 |
| `search_by_category()` | Filters expenses by category and shows total |
| `month_report()`       | Shows total monthly expense                  |
| `display_method()`     | Displays CLI options                         |
| `flow_func()`          | Handles main program flow                    |

Future Enhancements

Add formatted table output using tabulate

Add date range filters

Visualize expenses using matplotlib

Export reports to PDF

Convert into a FastAPI backend in future







