weight = int(input("Enter your weight in kg: "))
height = int(input("Enter your height in centimeters: "))
bmi = weight / ((height / 100) ** 2)
print("Your BMI is:", format(bmi, '.2f'))
