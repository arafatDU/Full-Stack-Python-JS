# The map() function executes a given function to each element of an iterable (such as lists, tuples, etc.).
def calculateSquare(n):
    return n*n

numbers = (1, 2, 3, 4)
result = map(calculateSquare, numbers)
print(result)

# converting map object to set
numbersSquare = set(result)
print(numbersSquare)





# Example 2: map() with Lambda
numbers = (1, 2, 3, 4)
result = map(lambda x: x*x, numbers)
print(result)

# converting map object to set
numbersSquare = set(result)
print(numbersSquare)






# Example 3: map() passed two iterables after a function.
num1 = [4, 5, 6]
num2 = [5, 6, 7]

# adds corresponding items from the num1 and num2 lists
result = map(lambda n1, n2: n1+n2, num1, num2)
print(list(result))