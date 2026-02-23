# Temperature Converter

while True:
    # Displaying menu
    print("\n=== TEMPERATURE CONVERTER ===")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")
    print("7. Exit")

    # Take user choice
    choice = int(input("Enter your choice: "))

    # Option 1: Celsius to Fahrenheit
    if choice == 1:
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * 9/5) + 32   # formula for C → F
        print("Temperature in Fahrenheit =", round(fahrenheit, 2))

    # Option 2: Fahrenheit to Celsius
    elif choice == 2:
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9   # formula for F → C
        print("Temperature in Celsius =", round(celsius, 2))

    # Option 3: Celsius to Kelvin
    elif choice == 3:
        celsius = float(input("Enter temperature in Celsius: "))
        kelvin = celsius + 273.15           # formula for C → K
        print("Temperature in Kelvin =", round(kelvin, 2))

    # Option 4: Kelvin to Celsius
    elif choice == 4:
        kelvin = float(input("Enter temperature in Kelvin: "))
        celsius = kelvin - 273.15           # formula for K → C
        print("Temperature in Celsius =", round(celsius, 2))

    # Option 5: Fahrenheit to Kelvin
    elif choice == 5:
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        kelvin = (fahrenheit - 32) * 5/9 + 273.15   # formula for F → K
        print("Temperature in Kelvin =", round(kelvin, 2))

    # Option 6: Kelvin to Fahrenheit
    elif choice == 6:
        kelvin = float(input("Enter temperature in Kelvin: "))
        fahrenheit = (kelvin - 273.15) * 9/5 + 32   # formula for K → F
        print("Temperature in Fahrenheit =", round(fahrenheit, 2))

    # Option 7: Exit program
    elif choice == 7:
        print("Exiting program")
        break

    # Invalid input 
    else:
        print("Invalid choice! Please enter a number from 1 to 7.")