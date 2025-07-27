FAHRENHEIT_TO_CELSIUS_FACTOR=5/9
CELSIUS_TO_FAHRENHEIT_FACTOR=9/5.0

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
        temprature = input("Enter the temperature to convert: ")
        degree = input("Is this temperature in Celsius or Fahrenheit? (C/F):").strip().upper()
        if degree not in ['C', 'F']:
            print("Invalid temperature. Please enter a numeric value.")
            continue
        if degree == 'C':
            converted_temp = convert_to_fahrenheit(float(temprature))
            print(f"{temprature}°C is {converted_temp:.2f}°F")
        else:
            converted_temp = convert_to_celsius(float(temprature))
            print(f"{temprature}°F is {converted_temp:.2f}°C")
        if input("Do you want to perform another conversion? (yes/no): ").strip().lower() != 'yes':
            print("Exiting the Temperature Conversion Tool. Goodbye!")
            break
if __name__ == "__main__":
    main()