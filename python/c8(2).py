#Write a python program using function to convert Celsius to Fahrenheit and vice_versa.

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9


choice = input("Enter 'C' for Celsius to Fahrenheit conversion or 'F' for Fahrenheit to Celsius conversion: ").upper()

if choice == 'C':
    celsius = float(input("Enter temperature in Celsius: "))
    print(f"{celsius}°C is equal to {celsius_to_fahrenheit(celsius):.2f}°F")
elif choice == 'F':
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    print(f"{fahrenheit}°F is equal to {fahrenheit_to_celsius(fahrenheit):.2f}°C")
else:
    print("Invalid choice. Please enter 'C' or 'F'.")
