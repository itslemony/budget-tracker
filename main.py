# library imports
import json
from storage import save_data, load_data

# variables
budget = 0
recent_expenses_length = 5
recent_expenses = []

budget, recent_expenses = load_data()

def add_expense(amount):
    global budget

    if amount > budget:
        print("Insufficient budget to add this expense.")
        return False

    budget -= amount
    return True

def add_income(amount):
    global budget
    budget += amount
    save_data(budget, recent_expenses)  # Save data after adding income

def get_recent_expenses():
    if not recent_expenses:
        print("No recent expenses to display.")
        return
    for expense in recent_expenses[-recent_expenses_length:]:
        for category, amount in expense.items():
            print(f"Category: {category}, Amount: ${amount}")

    choice = input("Clear recent expenses? (y/n): ")
    if choice == 'y':
        recent_expenses.clear()
        save_data(budget, recent_expenses)
    elif choice == 'n':
        return
    else:
        print("Invalid choice. Please enter 'y' or 'n'.")
        get_recent_expenses()  # Call the function again for valid input
        

def display_menu():
    print("==== Budget Tracker ====")
    print("Current Budget: $", budget)
    print("1. Add Expense")
    print("2. Add Income")
    print("3. View Expenses")
    print("4. Exit")
    

    return input("Choice: ")

def track_expense():
    print("Enter the category of the expense (e.g., Food, Transport, Entertainment): ")
    category = input("Category: ")
    print("Enter the amount of the expense: ")
    amount = input("Amount: $")
    if not amount.isdigit():
        print("Invalid input. Please enter a numeric value.")
        return
    print(f"Expense of ${amount} added to category: {category}")
    add_expense(int(amount))
    recent_expenses.append({category: int(amount)})
    save_data(budget, recent_expenses)  # Save data after adding expense

def main():
    while True:
        choice = display_menu()
        if choice == '1':
            track_expense()
        elif choice == '2':
            amount = input("Enter income amount: $")
            if not amount.isdigit():
                print("Invalid input. Please enter a numeric value.")
                continue
            add_income(int(amount))
            print("Income added. New budget: $", budget)
        elif choice == '3':
            get_recent_expenses()
        elif choice == '4':
            print("Exiting Budget Tracker.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()