# Number Pattern Printer

print("Choose Pattern:")
print("1. Pattern 1")
print("2. Pattern 2")
print("3. Pattern 3")
print("4. Pattern 4")

choice = int(input("Enter pattern number: "))
height = int(input("Enter height: "))

# Pattern 1
# 1
# 1 2
# 1 2 3
if choice == 1:
    for i in range(1, height + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

# Pattern 2 
# 1
# 2 2
# 3 3 3
elif choice == 2:
    for i in range(1, height + 1):
        for j in range(i):
            print(i, end=" ")
        print()

#  Pattern 3 
# 5 4 3 2 1
# 4 3 2 1
elif choice == 3:
    for i in range(height, 0, -1):
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()

# Pattern 4
# 1
# 121
# 12321
elif choice == 4:
    for i in range(1, height + 1):
        # ascending numbers
        for j in range(1, i + 1):
            print(j, end="")
        # descending numbers
        for j in range(i - 1, 0, -1):
            print(j, end="")
        print()

else:
    print("Invalid choice")