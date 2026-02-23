# Age Calculator (with Bonus)

from datetime import date

# take input from user for full birth date
birth_day = int(input("Enter birth day: "))
birth_month = int(input("Enter birth month: "))
birth_year = int(input("Enter birth year: "))

# Storing today's date
today = date.today()

# Creating birth date variable
birth_date = date(birth_year, birth_month, birth_day)

# Calculating total days lived
total_days_lived = (today - birth_date).days

# Converting into other units
current_age = total_days_lived // 365
age_in_months = current_age * 12
age_in_days = total_days_lived
age_in_hours = age_in_days * 24
age_in_minutes = age_in_hours * 60

# Years until 100
years_until_100 = 100 - current_age

# Display results
print("Current age:", current_age)
print("Age in months:", age_in_months)
print("Age in days:", age_in_days)
print("Age in hours:", age_in_hours)
print("Age in minutes:", age_in_minutes)
print("Years until age 100:", years_until_100)