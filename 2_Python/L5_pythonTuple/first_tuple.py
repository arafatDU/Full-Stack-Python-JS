fruits = ("mango", "banana", "apple", 1, 2)
print(fruits)
print(type(fruits))
# One item tuple
user_name = ("arafat",)   # without comma -> str
print(type(user_name))


# Accessing Tuple
print(fruits[-1])


# Update Tuple ---> Tuple can't be change directly, make it List first
fruits = list(fruits)
print(fruits)
fruits.append("orange")
fruits.append(5)
fruits.remove(2)
fruits.remove(1)
fruits = tuple(fruits)
print(fruits)


# Loop on Tuple
for fruit in fruits:
    print(fruit)

"""
for i in range(len(fruits)):
    print(fruits[i])
"""
print("----------------")
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1



# joining tuple
odd_numbers = (1, 3, 5)
even_numbers = (2, 4, 8)

numbers = odd_numbers + even_numbers + user_name
print(numbers)

