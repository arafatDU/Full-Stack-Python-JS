# solution of ax^2 + bx + c = 0
import math
print("ax^2 + bx + c = 0\n")
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

x1 = int((-b + math.sqrt(b*b - 4*a*c))/2*a)
x2 = int((-b - math.sqrt(b*b - 4*a*c))/2*a)

print("Solution is (" + str(x1) + " ," + str(x2) + ")")
