# Factorial Calculator using loop

# take input from user
num = int(input("Enter a number: "))

# Check for negative number
if num < 0:
    print("Factorial is not defined for negative numbers.")

# Factorial of 0 is 1
elif num == 0:
    print("0! = 1")

else:
    factorial = 1        # to store result
    steps = ""           # to store multiplication steps

    # Loop from number to 1
    for i in range(num, 0, -1):
        factorial *= i
        
        # Build step string
        steps += str(i)
        if i != 1:
            steps += " × "

    # Print result in required format
    print(f"{num}! = {steps} = {factorial}")