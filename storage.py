from models import Expense 
import json


def load_expenses():
    exps=[]

    try:
        with open("data/expenses.json") as file:
            data=json.load(file)

    except FileNotFoundError:
        print("Expenses file not found. Starting with an empty expense list.")
        return []
    
    for item in data:
        exp = Expense(
            item["id"],
            item["amount"],
            item["category"],
            item["description"],
            item["date"]
        )
        exps.append(exp)    
    return exps

def save_expenses(expenses):
    data=[]
    for i in expenses:
        data.append(i.__dict__)

    with open("data/expenses.json", "w") as file:
        json.dump(data, file, indent=4)