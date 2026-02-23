# 1. Factorial
def factorial(n):
    if n < 0:
        return "Factorial not defined for negative numbers"
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact


# 2. Prime Check
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


# 3. Fibonacci (nth number)
def fibonacci(n):
    if n < 0:
        return "Invalid input"
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


# 4. Sum of digits
def sum_of_digits(n):
    return sum(int(d) for d in str(abs(n)))


# 5. Reverse number
def reverse_number(n):
    sign = -1 if n < 0 else 1
    return sign * int(str(abs(n))[::-1])


# 6. Armstrong number check
def is_armstrong(n):
    digits = str(abs(n))
    power = len(digits)
    total = sum(int(d)**power for d in digits)
    return total == abs(n)


# 7. GCD (Euclidean algorithm)
def gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)


# 8. LCM
def lcm(a, b):
    if a == 0 or b == 0:
        return 0
    return abs(a*b) // gcd(a, b)


# 9. Perfect number check
def is_perfect_number(n):
    if n <= 0:
        return False
    divisors_sum = 0
    for i in range(1, n//2 + 1):
        if n % i == 0:
            divisors_sum += i
    return divisors_sum == n


# 10. Menu function
def math_menu():
    while True:
        print("\n=== NUMBER SYSTEM MENU ===")
        print("1. Factorial")
        print("2. Prime Check")
        print("3. Fibonacci")
        print("4. Sum of Digits")
        print("5. Reverse Number")
        print("6. Armstrong Check")
        print("7. GCD")
        print("8. LCM")
        print("9. Perfect Number Check")
        print("10. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            n = int(input("Enter number: "))
            print("Factorial:", factorial(n))

        elif choice == "2":
            n = int(input("Enter number: "))
            print("Prime?" , is_prime(n))

        elif choice == "3":
            n = int(input("Enter n: "))
            print("Fibonacci:", fibonacci(n))

        elif choice == "4":
            n = int(input("Enter number: "))
            print("Sum of digits:", sum_of_digits(n))

        elif choice == "5":
            n = int(input("Enter number: "))
            print("Reversed:", reverse_number(n))

        elif choice == "6":
            n = int(input("Enter number: "))
            print("Armstrong?", is_armstrong(n))

        elif choice == "7":
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            print("GCD:", gcd(a, b))

        elif choice == "8":
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            print("LCM:", lcm(a, b))

        elif choice == "9":
            n = int(input("Enter number: "))
            print("Perfect number?", is_perfect_number(n))

        elif choice == "10":
            print("Exiting program...")
            break

        else:
            print("Invalid choice! Try again.")


# Run the menu
math_menu()