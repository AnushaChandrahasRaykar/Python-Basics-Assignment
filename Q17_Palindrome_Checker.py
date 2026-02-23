# PALINDROME CHECKER
# Checks if word or number reads same forward and backward
# Ignores case and shows verification steps

text = input("Enter word/number: ")

# storing original input for display
original = text

# converting to lowercase for checking
check_text = text.lower()

# reverse using slicing
reversed_text = check_text[::-1]

# display steps
print("Original:", original)
print("Reversed:", reversed_text)

# check palindrome
if check_text == reversed_text:
    print("Result: PALINDROME")
else:
    print("Result: NOT PALINDROME")