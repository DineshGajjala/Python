#a leap year is a year that is divisible by 4 but not divisible by 100, or it is divisible by 400. 
# This means that a leap year has an extra day (February 29) compared to a common year, 
# which has 365 days. The leap year helps to keep the calendar year synchronized with the 
# astronomical year.
num=int(input("Enter a year:"))
if (num%4==0 and num%100!=0) or (num%400==0): #num%100!=0 is used to check if the year is not divisible by 100
    print(num,"is a leap year.")
else:
    print(num,"is not a leap year.")