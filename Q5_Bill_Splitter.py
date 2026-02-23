# Restaurant Bill Splitting

# Taking inputs from user
total_bill = float(input("Enter total bill: "))
num_people = int(input("Number of people: "))
tax_percent = float(input("Tax percentage: "))
tip_percent = float(input("Tip percentage: "))

# Subtotal
subtotal = total_bill

# Calculating tax amount
tax_amount = subtotal * tax_percent / 100

# Bill after adding tax
bill_after_tax = subtotal + tax_amount

# Calculating tip on bill after tax
tip_amount = bill_after_tax * tip_percent / 100

# Final total bill
total_final = bill_after_tax + tip_amount

# Amount per person
per_person = total_final / num_people

# Displaying breakdown of bill
print("=== BILL BREAKDOWN ===")
print("Subtotal: ₹{:.2f}".format(subtotal))    #.2f for printing numbers with exactly 2 decimal places
print("Tax ({}%): ₹{:.2f}".format(tax_percent, tax_amount))
print("After tax: ₹{:.2f}".format(bill_after_tax))
print("Tip ({}%): ₹{:.2f}".format(tip_percent, tip_amount))
print("Total: ₹{:.2f}".format(total_final))
print("Per person: ₹{:.2f}".format(per_person))