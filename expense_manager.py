# expense_manager.py

import json
from datetime import datetime

FILENAME = "expenses.txt"

# Load existing expenses from file
try:
    with open(FILENAME, "r") as file:
        expenses = json.load(file)
except (FileNotFoundError, json.JSONDecodeError):
    expenses = []

def save_expenses():
    """Save the current expenses list to file"""
    with open(FILENAME, "w") as file:
        json.dump(expenses, file)

def add_expense(date, category, amount, description):
    """Add a new expense and save it"""
    expense = {
        "date": date,
        "category": category,
        "amount": amount,
        "description": description
    }
    expenses.append(expense)
    save_expenses()
    print("Expense added successfully!")

def show_expenses(filtered=None, sort_by=None):
    """Display expenses, optionally filtered or sorted"""
    data = filtered if filtered is not None else expenses

    if not data:
        print("No expenses found.")
        return

    # Sort if required
    if sort_by == "date":
        data.sort(key=lambda x: x["date"])
    elif sort_by == "amount":
        data.sort(key=lambda x: x["amount"])

    # Print header
    print("\n{:<5} {:<12} {:<15} {:<10} {:<30}".format("No.", "Date", "Category", "Amount", "Description"))
    print("-"*75)
    for i, exp in enumerate(data, 1):
        print("{:<5} {:<12} {:<15} {:<10} {:<30}".format(
            i, exp["date"], exp["category"], exp["amount"], exp["description"]
        ))

def total_expenses(filtered=None):
    """Calculate and display the total amount spent"""
    data = filtered if filtered is not None else expenses
    total = sum(exp["amount"] for exp in data)
    print(f"\nTotal Expenses: {total}")

def filter_by_category(category):
    """Return a list of expenses for a specific category"""
    return [exp for exp in expenses if exp["category"].lower() == category.lower()]

def filter_by_month(month, year):
    """Return a list of expenses for a specific month/year"""
    filtered = []
    for exp in expenses:
        try:
            dt = datetime.strptime(exp["date"], "%Y-%m-%d")
            if dt.month == month and dt.year == year:
                filtered.append(exp)
        except ValueError:
            continue
    return filtered