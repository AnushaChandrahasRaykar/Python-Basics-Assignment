# Simple Calculator Program

# Take two numbers from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Performing operations
add = num1 + num2
sub = num1 - num2
mul = num1 * num2
div = num1 / num2
mod = num1 % num2
exp = num1 ** num2   # exponent

# Displaying results
print("\nResults:")
print(num1, "+", num2, "=", add)
print(num1, "-", num2, "=", sub)
print(num1, "*", num2, "=", mul)
print(num1, "/", num2, "=", round(div, 2))
print(num1, "%", num2, "=", mod)
print(num1, "^", num2, "=", exp)