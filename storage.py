import csv

def save_expense(row):
    with open("expenses.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(row)