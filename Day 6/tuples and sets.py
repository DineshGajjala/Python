f=("app","battery","charger")
print(f)
print(f[0])
#A tuple cannot be modified
###Sets
#A set is a collection of unique values
a={1,2,3,3,4}
print(a)
a.add(5)
print(a)
a.remove(4)
print(a)
b={5,6,7,8,9}
print(a.union(b))
print(a.intersection(b))
