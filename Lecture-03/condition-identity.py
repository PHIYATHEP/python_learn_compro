a = [1, 2, 3]
b = a
c = [1, 2, 3]
d = [1, 2, 3]

print(a is b)  # True, because b references the same object as a
print(a is c)  # False, because c is a different object with the same content
print(c is d)  # False, because c and d are different objects with the same content

print(a == c)  # True, because a and c have the same content
print(c == d)  # True, because c and d have the same content