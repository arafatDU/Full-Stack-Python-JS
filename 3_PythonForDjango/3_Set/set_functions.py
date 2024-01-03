'''
Built-in Functions with Set
Built-in functions like all(), any(), enumerate(), len(), max(), min(), sorted(), sum() 
etc. are commonly used with sets to perform different tasks.

Function	Description
all()	    Returns True if all elements of the set are true (or if the set is empty).
any()	    Returns True if any element of the set is true. If the set is empty, returns False.
enumerate()	Returns an enumerate object. It contains the index and value for all the items of the set as a pair.
len()	    Returns the length (the number of items) in the set.
max()	    Returns the largest item in the set.
min()	    Returns the smallest item in the set.
sorted()	Returns a new sorted list from elements in the set(does not sort the set itself).
sum()	    Returns the sum of all elements in the set.
'''



# Python enumerate()
grocery = {'bread', 'milk', 'butter'}
enumerateGrocery = enumerate(grocery)

print(type(enumerateGrocery))

# converting to list
print(list(enumerateGrocery))

# changing the default counter
enumerateGrocery = enumerate(grocery, 10)
print(list(enumerateGrocery))





# Example 2: Looping Over an Enumerate object
grocery = {'bread', 'milk', 'butter'}

for item in enumerate(grocery):
    print(item)

print()

for count, item in enumerate(grocery):
    print(count, item)

print()

# changing default start value
for count, item in enumerate(grocery, 100):
    print(count, item)