"""
# ----------------------The While LOOP-----------------------
i = 0
while i < 10:
    print("Hello World")
    i += 1



# ----Infinity loop and break statement
while True:
    passcode = input("Enter the passcode: ")
    if passcode == "arafat":
        break
print("Correct!  Infinity loop end!")



# -----Continue statement-------
while True:
    name = input("Who are you? ")
    if name != "arafat":
        continue
    passcode = input("Hello " + name + ", What is your passcode? ")
    if passcode == "1234":
        break
print("Break! & LOOP END!")
"""






"""
# range(starting, ending, increment or decrement)   = range(0, 10, 2)
# range(6) = range(0, 6, 1)
# -------------------------------The for LOOP----------------------------
for i in range(5):
    print(str(i) + " Hello World")
    

-----Arrays accessing with for loop----
fruits = ["apple", "banana", "cherry"]
for i in fruits:
    print(i)



# series = 1+2+3+4
summ = 0
for i in range(1, 5):
    summ += i
print(summ)



# series = 1^2 + 2^2 +3^2 +4^2
s = 0
for i in range(1, 5):
    s += i*i
print("The sum of the squre series = " + str(s))



# Odd series = 1 + 3 + 5 + 7 + 9
s = 0
for i in range(1, 10, 2):
    s += i
print("The sum of odd series = " + str(s))


# Even series = 2 + 4 + 6 + 8
s = 0
for i in range(2, 10, 2):
    s += i
print("The sum of even series = " + str(s))
"""


# complex series = 1 + (1 + 2) + (1 + 2 +3) + (1 + 2 + 3 +4)
s = 0
for i in range(1, 5):
    for j in range(1, i + 1):
        s += j
print("The sum of the complex series = " + str(s))

