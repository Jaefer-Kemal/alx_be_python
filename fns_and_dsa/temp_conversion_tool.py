FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
def convert_to_celsius(fahrenheit):
    result = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return  result

def convert_to_fahrenheit(celsius):
    result = celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32
    return result


temperture = float(input("Enter the temperature to convert: "))
degree = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

if degree == "F":
    result = f"{convert_to_celsius(temperture)}°C"
elif degree == "C": 
    result = f"{convert_to_fahrenheit(temperture)}°F"
print(f"{temperture}°{degree} is {result}")

    