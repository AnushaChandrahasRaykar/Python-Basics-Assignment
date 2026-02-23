# Leap Year Checker 
# A year is leap if:
# 1. Divisible by 4 AND
# 2. Not divisible by 100 OR divisible by 400

# Take input from user
year = int(input("Enter a year: "))

# Check leap year condition
if year % 4 == 0:
    if year % 100 != 0:
        print(year, "is a Leap Year")
        print("Reason: Divisible by 4 and not divisible by 100")

    elif year % 400 == 0:
        print(year, "is a Leap Year")
        print("Reason: Divisible by 400")

    else:
        print(year, "is NOT a Leap Year")
        print("Reason: Divisible by 100 but not by 400")

else:
    print(year, "is NOT a Leap Year")
    print("Reason: Not divisible by 4")