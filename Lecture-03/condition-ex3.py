number_hours = int(input("Enter the number of hours worked: "))
hourly_rate = float(input("Enter the hourly rate: "))

if(number_hours > 40):
    overtime_hours = number_hours - 40
    overtime_pay = (overtime_hours * hourly_rate * 1.5) + (40 * hourly_rate)
    print("The gross pay is: $", overtime_pay)
else:
    print("The gross pay is: $", number_hours * hourly_rate)