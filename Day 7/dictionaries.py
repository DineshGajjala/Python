# A dictionary stores the data in the form of key:value
a={"name":"dinesh","age":22}
print(a)
print(a["name"])
a["salary"]=0000
print(a)
a["age"]=25
a.pop("salary")
print(a)


#Dictionary methods

#get method
print(a.get("name"))

#key method
print(a.keys())

#values method
print(a.values())

#loop through dictionary
for key,value in a.items():
    print(key,":",value)