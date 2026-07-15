inchar = input("Input one  character: ")
if (inchar >= 'A' and inchar <= 'Z'):
    print("This is a uppercase letter.")
elif(inchar >= 'a' and inchar <= 'z'):
    print("This is a lowercase letter.")
elif(inchar >= '0' and inchar <= '9'):
    print("This is a digit.")
else:
    print("This is a special character.")