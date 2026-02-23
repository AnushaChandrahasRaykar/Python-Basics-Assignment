# Movie Ticket Pricing System

# Take inputs from user
age = int(input("Enter age: "))
day = input("Enter day of the week: ")
tickets = int(input("Enter number of tickets: "))

# Decide base ticket price based on age
if age < 3:
    base_price = 0
    category = "Free"
elif age <= 12:
    base_price = 150
    category = "Child"
elif age <= 59:
    base_price = 300
    category = "Adult"
else:
    base_price = 200
    category = "Senior"

# Check discount based on day
# Convert day to lowercase so user can type Monday/monday/MONDAY
day = day.lower()

if day in ["friday", "saturday", "sunday"]:
    discount_rate = 0.20   # 20% discount
else:
    discount_rate = 0      # no discount

# Step 4: Calculate prices
base_total = base_price * tickets
discount_amount = base_total * discount_rate
price_after_discount = base_total - discount_amount

# Step 5: Display bill
print("\n=== TICKET BILL ===")
print("Category:", category)
print("Base price per ticket: ₹", base_price)
print("Total before discount: ₹", base_total)

if discount_rate > 0:
    print("Discount applied: 20%")
    print("Discount amount: ₹", discount_amount)
else:
    print("No discount applied")

print("Price after discount: ₹", price_after_discount)
print("Total amount to pay: ₹", price_after_discount)