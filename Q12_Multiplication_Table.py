# Multiplication Table Generator (with Bonus)

#choice
print("1. Single Table")
print("2. Full Table Grid (Bonus)")

choice = int(input("Enter your choice: "))

# Normal Question
if choice == 1:
    num = int(input("Enter number: "))
    end = int(input("Enter range (end): "))

    print("\nMultiplication Table of", num)
    for i in range(1, end + 1):
        print(num, "x", i, "=", num*i)

# Bonus Question
elif choice == 2:
    print("\nFULL MULTIPLICATION TABLE (1-10)\n")

    # Column headings
    print("   ", end="")
    for i in range(1, 11):
        print(f"{i:4}", end="")
    print()

    print("-" * 45)

    # Table rows
    for i in range(1, 11):
        print(f"{i:2} |", end="")
        for j in range(1, 11):
            print(f"{i*j:4}", end="")
        print()

else:
    print("Invalid choice")