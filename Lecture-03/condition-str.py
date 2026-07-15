str1= "Mary"
str2= "Mark"

# Compare the strings
if str1 == str2:
    print(f"{str1} and {str2} are equal.")
else:
    print(f"{str1} and {str2} are not equal.")

# Compare the strings lexicographically
if str1 < str2:
    print(f"{str1} comes before {str2} in lexicographical order.")
elif str1 > str2:
    print(f"{str1} comes after {str2} in lexicographical order.")

# Compare the strings case-insensitively
if(str1.lower() == str2.lower()):
    print(f"{str1} and {str2} are equal when case is ignored.")
else:
    print(f"{str1} and {str2} are not equal when case is ignored.")