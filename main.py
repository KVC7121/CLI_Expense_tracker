import services


def display_menu():
    
    print("""
          
          Please take a look at the Menu 👇
          
          1. Add Expense
          2. View Expenses
          3. Search by Category
          4. Search by Description
          5. View the Category Summary
          6. Delete Expense
          7. Clear All Expenses
          8. Exit
          """)

def main():
    print("\nHi!")
    while(True):
        display_menu()

        k= services.get_valid_int("Enter the choice of service from the menu: ")

        if k==8:
            break
        
        if k==1:
            services.add_expense()
        elif k==2:
            services.view_expenses()
        elif k==3:
            cat=services.get_valid_str("Please enter the category to find: ")
            services.search_by_category(cat)
        elif k==4:
            desc=services.get_valid_str("Please enter the description keywords to find: ")
            services.search_by_description(desc)
        elif k==5:
            services.category_summary()
        elif k==6:
            delete_id=services.get_valid_int("Enter the ID of the expense to delete: ")
            services.delete_expense(delete_id)
        elif k==7:
            services.clear_expenses()
        else:
            print("Please choose a valid service option from the menu (1 to 7)")
           
    print("\nThanks! See you next time.")        


if __name__ == "__main__":
    main()