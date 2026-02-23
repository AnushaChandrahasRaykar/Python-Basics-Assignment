# Sum and Average Calculator

# Ask user how many numbers they want to enter
count = int(input("How many numbers? "))

# Initialize variables
total = 0              # to store sum
maximum = None         # to store max value
minimum = None         # to store min value

# Loop to take inputs
for i in range(1, count + 1):
    num = float(input(f"Enter number {i}: "))

    # Add to total
    total += num

    # Check for maximum
    if maximum is None or num > maximum:
        maximum = num

    # Check for minimum
    if minimum is None or num < minimum:
        minimum = num

# Calculate average
average = total / count

# Display results
print("\nResults:")
print("Sum:", total)
print("Average:", average)
print("Maximum:", maximum)
print("Minimum:", minimum)