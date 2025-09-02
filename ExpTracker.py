import pandas as pd
import matplotlib.pyplot as plt
import os

# File to store expenses
FILE_NAME = "expenses.csv"

# Make sure the file exists
if not os.path.exists(FILE_NAME):
    df = pd.DataFrame(columns=["Date", "Category", "Amount", "Description"])
    df.to_csv(FILE_NAME, index=False)

# to add a new expense 
def add_expense(date, category, amount, description=""):
    df = pd.read_csv(FILE_NAME)
    new_expense = {"Date": date, "Category": category, "Amount": amount, "Description": description}
    df = pd.concat([df, pd.DataFrame([new_expense])], ignore_index=True)
    df.to_csv(FILE_NAME, index=False)
    print("✅ Expense added!")

#to show summary of the expenses 
def show_expenses():
    df = pd.read_csv(FILE_NAME)
    if df.empty:
        print("No expenses to show")
        return
    summary = df.groupby("category")['amount'].sum()
    print("\n expense Summary by Category :\n"), summary 

# to show a graph of the expenses 
def plot_expenses():
    df = pd.read_csv(FILE_NAME)
    if df.empty:
        print("No data to plot!")
        return
    summary = df.groupby("Category")["Amount"].sum()
    summary.plot(kind="bar")
    plt.title("Expenses by Category")
    plt.xlabel("Category")
    plt.ylabel("Amount")
    plt.tight_layout()
    plt.show()

# main program loop
while True:
    print("\nExpense Tracker Menu:")
    print("1. Add Expense")
    print("2. Show Expenses")
    print("3. Plot Expenses")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        date = input("Enter date (YYYY-MM-DD): ")
        category = input("Enter category: ")
        amount = float(input("Enter amount: "))
        desc = input("Enter description (optional): ")
        add_expense(date, category, amount, desc)
    elif choice == "2":
        show_expenses()
    elif choice == "3":
        plot_expenses()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again.")

