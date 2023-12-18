# swapping two number
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("First one: "+str(num1))
print("Second one: "+str(num2))

print("---------After swapping----------")
""" 
temp = num1
num1 = num2
num2 = temp 
"""
num1 += num2
num2 = num1 - num2
num1 -= num2
print("First one: "+str(num1))
print("Second one: "+str(num2))