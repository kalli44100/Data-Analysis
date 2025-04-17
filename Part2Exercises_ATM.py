pin_user = 1234
pin = 0
access = False
balance = 5000.50


pin = int(input("Enter your PIN..."))
if pin_user == pin:
    access = True

if access:
    # amount = 0.0
    print("Access granted")
    while True:
        menu = int(input("1 for Balance\n 2 to deposit\n 3 to withdraw\n 4 to exit\n"))
        if menu == 1:
            print("Your balance is $", str(balance))
            print("Would you like to perform another operation?")
        elif menu == 2:
            amount = 0
            depos = int(
                input("1 for $50\n 2 for $100\n 3 for $250\n 4 for custom amount\n")
            )
            if depos == 1:
                amount += 50
            elif depos == 2:
                amount += 100
            elif depos == 3:
                amount += 250
            elif depos == 4:
                amount = int(input("Enter the amount you want to deposit..."))
            else:
                print("Invalid choice. Please try again.")
            balance += amount
            print("Amount deposited successfully. New Balance is $", str(balance))
            print("Would you like to perform another operation?")
        elif menu == 3:
            amount = int(input("Enter the amount you want to withdraw..."))
            if amount <= balance:
                balance -= amount
                print("Amount withdrawn successfully. New balance is $", str(balance))
                print("Would you like to perform another operation?")
            else:
                print("Insufficient funds.")
                print("Would you like to perform another operation?")
        elif menu == 4:
            print("GoodBye")
            break
        else:
            print("Invalid choice. Please try again.")


else:
    print("Access denied")
