numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# slice -> numbers[start: end: step] start = 0, end = -1, step = 1
print(numbers[2:6])
print(numbers[:6])
print(numbers[2:])
# reverse the list by slicing -> start = -1, end = -11(default), step = -1
print(numbers[-1::-1])



# sorting a list
numbers_two = [1, 2, 4, 5, 10, 100]
numbers_two.sort()    # Ascending order
print(numbers_two)
numbers_two.sort(reverse=True)    # Descending order
print(numbers_two)

# sorted()
sorted_numbers_asc = sorted(numbers_two)
print("New sorted list(asc): " + str(sorted_numbers_asc))
sorted_numbers_des = sorted(numbers_two, reverse=True)
print("New sorted list(des): " + str(sorted_numbers_des))



# copy a list: 1. copy() method 2. slicing
numbers_clone = numbers.copy()
print(numbers_clone)
numbers_clone_two = numbers[:]
print(numbers_clone_two)


# join list: 1. add two or more(+) 2. extend() method
num_one = [1, 3, 4, 5, 6]
num_two = [7, 8, 9]
num_three = [10, 13]
merged_num = num_one + num_two + num_three
print("The joint list: " + str(merged_num))
# using extend() method
fruits = ["Mango", "Banana", "Jack", "Guava"]
fruit_one = ["Litchi"]
fruits.extend(fruit_one)
print(fruits)


