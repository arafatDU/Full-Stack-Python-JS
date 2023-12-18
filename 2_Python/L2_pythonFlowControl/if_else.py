"""
if 4 > 3:
    print("This is the first line")
    print("This is the second line")
elif 5 < 2:
    print("I am from elif block")
else:
    print("The condition is false")
    print("I am inside the else block")
print("I am from outside of if else block")
"""

print("1. Celcius to Fahrenheit\n2. Fahrenheit to Celcius\n")
choice = int(input("Enter your choice(1/2): "))
if choice == 1:
    celcius = float(input("Enter the celcius temperature: "))
    print("Fahrenheit: " + str(9/5 * celcius + 32) + " Degree")
elif choice == 2:
    fahrenheit = float(input("Enter the fahrenheit temperature: "))
    print("Celcius: " + str((fahrenheit - 32) * 5/9) + " Degree")
else:
    print("Invalid choice!")

