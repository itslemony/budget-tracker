import json

FILE_NAME = "budget_data.json"

def save_data(budget, recent_expenses):
    data = {
        "budget": budget,
        "recent_expenses": recent_expenses
    }
    with open(FILE_NAME, 'w') as file:
        json.dump(data, file, indent=4)

def load_data():
    try:
        with open(FILE_NAME, "r") as file:
            data = json.load(file)

        budget = data["budget"]
        recent_expenses = data["recent_expenses"]

        return budget, recent_expenses

    except FileNotFoundError:
        return 0, []
    
    