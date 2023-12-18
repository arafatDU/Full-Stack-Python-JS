# Leap year checking

year = int(input("Enter a year: "))
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print("The year " + str(year) + " is a Leap year!")
else:
    print("The year " + str(year) + " is not a Leap year.")

