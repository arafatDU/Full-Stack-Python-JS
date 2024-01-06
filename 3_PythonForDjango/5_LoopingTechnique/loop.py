# Python for Loop
languages = ['Swift', 'Python', 'Go', 'JavaScript']

# run a loop for each item of the list
for language in languages:
    print(language)
    
    
    
    
# Loop through a string
for x in 'Python':
    print(x)
    
    

# Python for Loop with Python range()
# use of range() to define a range of values
values = range(4)

# iterate from i = 0 to i = 3
for i in values:
    print(i)
    



# Using loop without accessing item
languages = ['Swift', 'Python', 'Go']

for _ in languages:
    print('Hello')
    print('Hi')
    





# python while loop
# program to display numbers from 1 to 5

# initialize the variable
i = 1
n = 5

# while loop from i = 1 to 5
while i <= n:
    print(i)
    i = i + 1
    
    


# Example 2: Python while loop
# program to calculate the sum of numbers
# until the user enters zero

total = 0
number = int(input('Enter a number: '))

# add numbers until number is zero
while number != 0:
    total += number    # total = total + number
    
    # take integer input again
    number = int(input('Enter a number: '))
    

print('total =', total)




# Using break & continue
# program to print odd numbers from 1 to 10

num = 0

while num < 10:
    num += 1
    
    if (num % 2) == 0:
        continue

    print(num)