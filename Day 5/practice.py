l=[20,30,25,40,60]
print("maximum number is:",max(l))
print("minimum number is:",min(l))
print("sum of numbers is:",sum(l))
count=0
for num in l:
    if num%2==0:
        count=count+1
print("even numbers in the list:",count)
print(l[::-1])