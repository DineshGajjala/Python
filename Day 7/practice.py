a={
    "name":"dino",
    "age":22,
    "course":"python"
}
print(a["name"])
a["fees"]=3000
print(a)
if "name" in a:
    print("Element found")
else:
    print("Element not found")



###counting frequency of a text
z="madam"
freq={}
for char in z:
    freq[char]=freq.get(char,0)+1
print(freq)
