# Example 01: Working with filter()
letters = ['a', 'b', 'd', 'e', 'i', 'j', 'o']

# a function that returns True if letter is vowel
def filter_vowels(letter):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return True if letter in vowels else False

filtered_vowels = filter(filter_vowels, letters)

# converting to tuple
vowels = tuple(filtered_vowels)
print(vowels)





# Example 2: Using Lambda Function Inside filter()
numbers = [1, 2, 3, 4, 5, 6, 7]

# the lambda function returns True for even numbers 
even_numbers_iterator = filter(lambda x: (x%2 == 0), numbers)

# converting to list
even_numbers = list(even_numbers_iterator)

print(even_numbers)






# Example 3: Using None as a Function Inside filter()
# random list
random_list = [1, 'a', 0, False, True, '0']

filtered_iterator = filter(None, random_list)

#converting to list
filtered_list = list(filtered_iterator)

print(filtered_list)

