keep_going = "y"
while keep_going == "y":
    sales = float(input("Enter sales amount: "))
    comm_rate = float(input("Enter commission rate: "))
    commission = sales * comm_rate
    print(f"Commission is: ${commission:.2f}")
    keep_going = input("Do you want to continue? (y/n): ")
