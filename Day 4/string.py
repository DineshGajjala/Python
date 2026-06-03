name=input("Enter a string that is like name:")
print(name)
print(name[0:3])
print(name[-6:-2])
print(name[0:6:2])
print(name.upper())
print(name.lower())
print(len(name))
print(name.replace("i","a"))
print(name[::-1])
if name==name[::-1]:
    print("The given string is a palindrome")
else:
    print("The given string is not a palindrome")
