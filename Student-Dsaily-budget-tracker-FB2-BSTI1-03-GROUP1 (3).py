    
from datetime import datetime

print("===== STUDENT DAILY BUDGET TRACKER =====")

while True:
    name = input("Enter your name: ").strip()

    if name and name.replace(" ", "").isalpha():
        break
    else:
        print("Invalid! Name must contain letters only.")

while True:
    Password = input("Enter your password: ").strip()

    if Password and Password.replace(" ","").isalpha():
        break
    else:
        print("Invalid! Password must contain numbers only. ")
    

print("\nLogin successful!")
print("Welcome,", name)

while True:
    try:
        budget = float(input("Enter your daily budget: ₱"))

        if budget > 0:
            break
        else:
            print("Invalid! Budget must be greater than 0.")

    except ValueError:
        print("Invalid! Please enter numbers only.")

expenses = []

while True:
    print("\n============== MAIN MENU ==============")
    print("[1] Add Expense")
    print("[2] Check Daily Budget")
    print("[3] Expense History")
    print("[4] Edit Daily Budget")
    print("[5] Exit")
    print("=======================================")

    choice = input("Choose an option: ").strip()

    if choice == "1":

        while True:
            print("\n========== ADD EXPENSE ==========")
            print("[1] Food") 
            print("[2] Transportation")
            print("[3] School Supplies")
            print("[4] Others")
            print("[5] Back to Main Menu")

            category_choice = input("Choose a category: ").strip()

            if category_choice == "5":
                break

            elif category_choice == "1":
                category = "Food"
                description = "Food"

            elif category_choice == "2":
                category = "Transportation"
                description = "Transportation"

            elif category_choice == "3":
                category = "School Supplies"
                description = "School Supplies"

            elif category_choice == "4":
                category = "Others"

                while True:
                    description = input(
                        "What did you spend on? "
                    ).strip()

                    if description:
                        break

                    print("Please enter a description.")

            else:
                print("Invalid category! Please choose 1-5.")
                continue

            
            total = sum(item[2] for item in expenses)
            remaining = budget - total

            if remaining <= 0:
                print("\nYour budget is already fully used!")
                break

            
            while True:
                try:
                    amount = float(
                        input("How much did you spend? ₱")
                    )           

                    if amount <= 0:
                        print("Amount must be greater than 0.")

                    elif amount > remaining:
                        print("Expense exceeds remaining budget.")
                        print(f"Remaining Balance: ₱{remaining:.2f}")

                    else:
                        break

                except ValueError:
                    print("Invalid! Please enter numbers only.")

            date_time = datetime.now().astimezone().strftime(
                "%Y-%m-%d %I:%M %p" 
            )

            expenses.append([
                category,
                description,
                amount,
                date_time
            ])

            total = sum(item[2] for item in expenses)
            remaining = budget - total

            print("\n================================")
            print("       EXPENSE RECORDED!")
            print("================================")
            print("Category:", category)
            print("Description:", description)
            print(f"Amount: ₱{amount:.2f}")
            print("Date & Time:", date_time)
            print(f"Remaining Balance: ₱{remaining:.2f}")

            if remaining <= 0:
                print("\nWARNING: Your budget is fully used!")

            elif remaining <= budget * 0.20:
                print("\nWARNING: You are almost out of budget!")
                print(f"Only ₱{remaining:.2f} remaining.")

            while True:
                print("\n[1] Add Another Expense")
                print("[2] Back to Main Menu")

                next_choice = input("Choose an option: ").strip()

                if next_choice in ("1", "2"):
                    break

                print("Invalid choice! Please choose 1 or 2.")

            if next_choice == "2":
                break

    elif choice == "2":
        total = sum(item[2] for item in expenses)
        remaining = budget - total

        print("\n================================")
        print("         DAILY BUDGET")
        print("================================")
        print(f"Student Name:      {name}")
        print(f"Daily Budget:      ₱{budget:.2f}")
        print(f"Total Expenses:    ₱{total:.2f}")
        print(f"Remaining Balance: ₱{remaining:.2f}")

        if remaining <= 0:
            print("Status: BUDGET FULLY USED")

        elif remaining <= budget * 0.20:
            print("Status: LOW BUDGET")
            print("Warning: You are almost out of budget!")

        else:
            print("Status: WITHIN BUDGET")

    elif choice == "3":
        print("\n================ EXPENSE HISTORY ================")

        if not expenses:
            print("No expenses recorded.")

        else:
            print("-" * 100)
            print(
                f"{'No.':<5}"
                f"{'Category':<22}"
                f"{'Description':<22}"
                f"{'Amount':<15}"
                f"{'Date & Time':<25}"
            )
            print("-" * 100)

            for i, item in enumerate(expenses, start=1):
                category = item[0]
                description = item[1]
                amount = item[2]
                date_time = item[3]

                print(
                    f"{i:<5}"
                    f"{category:<22}"
                    f"{description:<22}"
                    f"₱{amount:<14.2f}"
                    f"{date_time:<25}"
                )

            total = sum(item[2] for item in expenses)
            remaining = budget - total

            print("-" * 100)
            print(f"{'Daily Budget:':<25} ₱{budget:.2f}")
            print(f"{'Total Expenses:':<25} ₱{total:.2f}")
            print(f"{'Final Balance:':<25} ₱{remaining:.2f}")

            if remaining <= 0:
                print("Status: BUDGET FULLY USED")

            elif remaining <= budget * 0.20:
                print("Status: LOW BUDGET")

            else:
                print("Status: WITHIN BUDGET")

            print("-" * 100)

    elif choice == "4":
        total = sum(item[2] for item in expenses)

        print("\n================================")
        print("       EDIT DAILY BUDGET")
        print("================================")
        print(f"Current Budget:   ₱{budget:.2f}")
        print(f"Total Expenses:   ₱{total:.2f}")
        print(f"Current Balance:  ₱{budget - total:.2f}")

        print("\n[1] Change Daily Budget")
        print("\n[2] Back to Main Menu")    

        edit_choice = input("Choose an option: ").strip()

        if edit_choice == "1":
            while True:
                try:
                    new_budget = float(
                        input("Enter new daily budget: ₱")
                    )

                    if new_budget <= 0:
                        print("Budget must be greater than 0.")

                    elif new_budget < total:
                        print(
                            "New budget cannot be lower "
                            "than total expenses."
                        )
                        print(f"Total Expenses: ₱{total:.2f}")

                    else:
                        budget = new_budget

                        print("\nDaily budget updated successfully!")
                        print(f"New Budget: ₱{budget:.2f}")
                        print(
                            f"Remaining Balance: "
                            f"₱{budget - total:.2f}"
                        )
                        break

                except ValueError:
                    print("Invalid! Please enter numbers only.")

        elif edit_choice == "2":
            print("Returning to Main Menu...")

        else:
            print("Invalid choice! Please choose 1 or 2.")

    elif choice == "5":
        while True:
            print("\n========== EXIT ==========")
            print("[1] Yes, Exit")
            print("[2] No, Go Back")

            exit_choice = input("Choose an option: ").strip()

            if exit_choice in ("1", "2"):
                break

            print("Invalid choice! Please choose 1 or 2.")

        if exit_choice == "1":
            print(f"\nGoodbye, {name}!")
            print("Thank you for using the tracker.")
            break

    else:
        print("Invalid choice! Please choose 1-5.")
