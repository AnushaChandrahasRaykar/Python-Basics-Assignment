# PRIME NUMBER CHECKER
# Part 1: Check if a single number is prime
# Part 2: Print all prime numbers in a given range

# ---------- PART 1 : SINGLE NUMBER CHECK ----------
num = int(input("Enter a number: "))

# Negative numbers, 0 and 1 are not prime
if num <= 1:
    print(num, "is NOT a prime number")

# 2 is the only even prime number
elif num == 2:
    print("2 is a PRIME number")

else:
    is_prime = True

    # Check divisibility from 2 to num-1
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num, "is a PRIME number")
    else:
        print(num, "is NOT a prime number")


# ---------- PART 2 : PRIME NUMBERS IN RANGE ----------
start = int(input("Enter start range: "))
end = int(input("Enter end range: "))

print("Prime numbers:", end=" ")

for n in range(start, end + 1):

    if n <= 1:
        continue

    # Check if n is prime
    prime = True
    for i in range(2, n):
        if n % i == 0:
            prime = False
            break

    if prime:
        print(n, end=" ")