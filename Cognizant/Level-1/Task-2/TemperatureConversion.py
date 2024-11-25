value = float(input("Enter the temperature value: "))

unit = input("Enter the unit of measurement Celsius or Fahrenheit (C/F): ")
if unit == "C":
    result = value*(9/5)+32
    print("Temperature in Fahrenheit is = ",result, "°F")
elif unit == "F":
    result = (value-32)*(5/9)
    print("Temperature in Celsius is:",result,"°C")
else:
    print("Enter correct measurement!")