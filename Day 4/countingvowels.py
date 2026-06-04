name=input("Enter a string:")
vowels="aeiouAEIOU"
count=0
for i in name:
    if i in vowels:
        count=count+1
print("The no.of vowels in the given name is",count)