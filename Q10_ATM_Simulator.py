# Simple ATM Simulator
# Initial balance is 10000 and minimum balance must be 500

balance = 10000   # starting balance

while True:
    # Display menu
    print("\nATM SIMULATOR")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    # Option 1: Check balance
    if choice == 1:
        print("Current balance: ₹", balance)

    # Option 2: Deposit money
    elif choice == 2:
        amount = float(input("Enter amount to deposit: "))
        balance = balance + amount
        print("Deposit successful!")
        print("New balance: ₹", balance)

    # Option 3: Withdraw money
    elif choice == 3:
        amount = float(input("Enter amount to withdraw: "))

        # Check sufficient balance
        if amount > balance:
            print("Insufficient balance!")

        elif balance - amount < 500:
            print("Withdrawal not allowed!")
            print("Minimum balance of ₹500 must remain.")

        else:
            balance = balance - amount
            print("Withdrawal successful!")
            print("New balance: ₹", balance)

    # Option 4: Exit
    elif choice == 4:
        print("Thank you for using ATM.")
        break

    # Invalid input
    else:
        print("Invalid choice, try again.")