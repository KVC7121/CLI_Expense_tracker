from models import Expense
import storage

expenses=storage.load_expenses()

def add_expense():

    print("\nEnter the details of the expense")
    amount=get_valid_amount("Amount: ")
    category=get_valid_str("Category: ")
    description=get_valid_str("Description: ")
    date=get_valid_str("Date: ")

    exp=Expense(max((x.id for x in expenses), default=0)+1,amount,category,description,date)
    expenses.append(exp)
    storage.save_expenses(expenses)
    print("\nA new expense data is added successfulyy!")

def view_expenses():
    if not expenses:
        return print("\nNo expenses to view")

    print("\nAll expenses data:-\n")
    for i in expenses:
        print(i)
        print("\n")

def delete_expense(id_num: int):
    if len(expenses)==0:
        print("\nNo expenses to delete")
        return
    
    org_count=len(expenses)

    expenses[:]=[i for i in expenses if i.id!=id_num]

    if org_count==len(expenses):
        print(f"\nNo expense is found with the ID: {id_num}")
    else:     
        print(f"\nExpense with id:{id_num} is deleted")
        storage.save_expenses(expenses)

def search_by_category(catg):
    found=False
    for i in expenses:
        if i.category==catg:
            print(f"Match found with expense {i.id}")
            print(f"\n{i}")
            found=True
    if not found:
        print("\nMatch not found")        

def search_by_description(desc):
    found=False
    for i in expenses:
        if desc in i.description:
            print(f"Match found with expense {i.id}")
            print(f"\n{i}")
            found=True
    if not found:
        print("\nMatch not found") 

def category_summary():
    d={}
    for i in expenses:
        if i.category in d:
            d.update({i.category:d.get(i.category)+i.amount})
        else:
            d.update({i.category:i.amount})    

    print("\nSummary of expenses by category\n")

    for catg,total in d.items():
        print(f"{catg} --> ₹ {total}")
    print("\n")

def clear_expenses():
    if not expenses:
        print("\nNo expenses to clear.")
        return
    expenses.clear()
    storage.save_expenses(expenses)
    print("\nAll expenses have been cleared.\n")

# Handling inputs

def get_valid_str(msg):
    while True:
        value=input(msg).strip()

        if value:
            return value
        print("Input is empty. Please enter valid input")

def get_valid_amount(msg):
    while True:
        value=input(msg).strip()

        if not value:
            print("Input can't be empty.")
            continue

        try:
            amount=float(value)

            if amount<=0:
                print("Amount cannot be negative or zero")
                continue

            return amount
        
        except ValueError:
            print("Please enter valid amount")

def get_valid_int(msg):
    while True:
        value=input(msg).strip()

        if not value:
            print("Input can't be empty.")
            continue

        try:
            return int(value)
        except ValueError:
            print("Please enter valid input")

