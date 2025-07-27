FAHRENHEIT_TO_CELSIUS_FACTOR= 5.0 / 9.0
CELSIUS_TO_FAHRENHEIT_FACTOR = 9.0 / 5.0

def convert_to_celsius(fahrenheit): 
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def display_conversion_menu():
    print("Temperature Conversion Tool")
    print("1. Convert Fahrenheit to Celsius")
    print("2. Convert Celsius to Fahrenheit")
    print("3. Exit")

def main():
    while True:
        display_conversion_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            celsius = convert_to_celsius(fahrenheit)
            print(f"{fahrenheit}°F is {celsius:.2f}°C")
        elif choice == '2':
            celsius = float(input("Enter temperature in Celsius: "))
            fahrenheit = convert_to_fahrenheit(celsius)
            print(f"{celsius}°C is {fahrenheit:.2f}°F")
        elif choice == '3':
            print("Exiting the Temperature Conversion Tool. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()