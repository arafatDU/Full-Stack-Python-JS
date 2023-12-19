numbers = []
for i in range(1, 11):
    numbers.append(i)

print(numbers)

# List comprehensions
numbers_two = [i-1 for i in range(1, 101)]
print(numbers_two)


# List comprehension part 2
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = [num for num in numbers if num%2 == 0]
print("Even numbers: "+ str(even_numbers))

odd_numbers = [num for num in numbers if num%2 != 0]
print("Odd numbers: " + str(odd_numbers))


