# CALCULATOR USING FUNCTIONS
# Each operation is written as a separate function

# Addition function
def add(a, b):
    return a + b

# Subtraction function
def subtract(a, b):
    return a - b

# Multiplication function
def multiply(a, b):
    return a * b

# Division function (with zero check)
def divide(a, b):
    if b == 0:
        return "Error! Division by zero not allowed."
    return a / b

# Modulus function
def modulus(a, b):
    return a % b

# Power function
def power(a, b):
    return a ** b


# Main calculator function
def calculator():

    while True:
        print("\n=== FUNCTION CALCULATOR ===")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Modulus")
        print("6. Power")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        # Exit condition
        if choice == "7":
            print("Exiting calculator...")
            break

        # Take numbers from user
        if choice in ["1","2","3","4","5","6"]:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            # Call functions based on choice
            if choice == "1":
                result = add(num1, num2)

            elif choice == "2":
                result = subtract(num1, num2)

            elif choice == "3":
                result = multiply(num1, num2)

            elif choice == "4":
                result = divide(num1, num2)

            elif choice == "5":
                result = modulus(num1, num2)

            elif choice == "6":
                result = power(num1, num2)

            print("Result:", result)

        else:
            print("Invalid choice! Please select from menu.")


# calculatoion
calculator()