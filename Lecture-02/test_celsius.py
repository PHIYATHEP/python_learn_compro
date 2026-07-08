choice = str(input("You select Celsius (C) or Fahrenheit (F): "))
uppercase_choice = choice.upper()
if(uppercase_choice == "C"):
    celsius = int(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print("Temperature in Fahrenheit is:", format(fahrenheit, '.2f'))
elif(uppercase_choice == "F"):
    fahrenheit = int(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print("Temperature in Celsius is:", format(celsius, '.2f'))
else:
    print("Invalid input. Please select either 'C' for Celsius or 'F' for Fahrenheit.")