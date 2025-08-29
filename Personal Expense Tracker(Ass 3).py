import json
from datetime import datetime
import os

# File name (saved in the same folder as this script)
FILE_NAME = "expenses_data.json"

# ---------------- File Handling ---------------- #
def load_expenses():
    """Load expenses from file if available"""
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            return []
    return []

def save_expenses(expenses):
    """Save expenses to file"""
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)

# ---------------- View Summary ---------------- #
def view_summary(expenses):
    if not expenses:
        print("No expenses recorded yet.\n")
        return
    
    print("\n---- Expense Summary ----")
    total = sum(exp["amount"] for exp in expenses)
    print(f"Total Spending: ${total:.2f}")
    
    # Category-wise summary
    category_totals = {}
    for exp in expenses:
        category_totals[exp["category"]] = category_totals.get(exp["category"], 0) + exp["amount"]
    
    print("\nSpending by Category:")
    for category, amount in category_totals.items():
        print(f"{category}: ${amount:.2f}")
    
    print("--------------------------\n")

# ---------------- Add Expense ---------------- #
def add_expense(expenses):
    try:
        amount = float(input("Enter expense amount: "))
    except ValueError:
        print("❌ Invalid amount! Please enter a number.\n")
        return
    
    category = input("Enter category (Food, Transport, etc.): ")
    date = input("Enter date (YYYY-MM-DD) or press Enter for today: ")
    
    if not date:
        date = datetime.now().strftime("%Y-%m-%d")

    expense = {
        "amount": amount,
        "category": category,
        "date": date
    }
    expenses.append(expense)
    save_expenses(expenses)
    print("✅ Expense added successfully!\n")

    # 👇 Show updated summary immediately
    view_summary(expenses)

# ---------------- Main Menu ---------------- #
def main():
    expenses = load_expenses()
    
    while True:
        print("==== Personal Expense Tracker ====")
        print("1. Add Expense")
        print("2. View Summary")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_summary(expenses)
        elif choice == "3":
            print("Exiting... Have a great day! 👋")
            break
        else:
            print("❌ Invalid choice! Try again.\n")

if __name__ == "__main__":
    main()
