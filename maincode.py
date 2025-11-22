def length_conversion():
    print("\n-Length Conversion-")
    print("1. Kilometers to Meters")
    print("2. Meters to Kilometers")
    print("3. Meters to Centimeters")
    print("4. Centimeters to Meters")

    choice = input("Enter your choice (1-4): ")

    value = float(input("Enter the value to convert: "))

    if choice == "1":
        result = value * 1000       
        print(f"{value} km = {result} m")
    elif choice == "2":
        result = value / 1000      
        print(f"{value} m = {result} km")
    elif choice == "3":
        result = value * 100       
        print(f"{value} m = {result} cm")
    elif choice == "4":
        result = value / 100       
        print(f"{value} cm = {result} m")
    else:
        print("Invalid choice!")


def weight_conversion():
    print("\n-Weight Conversion-")
    print("1. Kilograms to Grams")
    print("2. Grams to Kilograms")

    choice = input("Enter your choice (1-2): ")

    value = float(input("Enter the value to convert: "))

    if choice == "1":
        result = value * 1000      
        print(f"{value} kg = {result} g")
    elif choice == "2":
        result = value / 1000       
        print(f"{value} g = {result} kg")
    else:
        print("Invalid choice!")


def temperature_conversion():
    print("\n-Temperature Conversion-")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

    choice = input("Enter your choice (1-2): ")

    value = float(input("Enter the temperature value: "))

    if choice == "1":
        result = (value * 9/5) + 32
        print(f"{value} °C = {result} °F")
    elif choice == "2":
        result = (value - 32) * 5/9
        print(f"{value} °F = {result} °C")
    else:
        print("Invalid choice!")


def main():
    while True:
        print("\n==UNIT CONVERSION SYSTEM==")
        print("1. Length Conversion")
        print("2. Weight Conversion")
        print("3. Temperature Conversion")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            length_conversion()
        elif choice == "2":
            weight_conversion()
        elif choice == "3":
            temperature_conversion()
        elif choice == "4":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")
          
      main()
