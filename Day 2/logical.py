marks=int(input("Enter marks:"))
if marks>100:
    print("Invalid marks")
elif marks>=75 and marks<=100:
    print("good")
elif marks>=50 or marks<25:
    print("average")
    
else:
    print("poor")