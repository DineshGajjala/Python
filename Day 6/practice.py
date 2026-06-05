a={1,23,4,5,6}
b={6,5,8,9,7}
print(a.intersection(b))
print(a.union(b))
c=[1,2,3,4,5,6,6,3]
z=list(set(c))
print(z)
g=int(input("Enter a number:"))
if g in a:
    print("Element found")
else:
    print("Elemenet not found")
