"""
List Methods
Python has many useful list methods that makes it really easy to work with lists.

Method	Description
append()	add an item to the end of the list
extend()	add all the items of an iterable to the end of the list
insert()	inserts an item at the specified index
remove()	removes item present at the given index
pop()	returns and removes item present at the given index
clear()	removes all items from the list
index()	returns the index of the first matched item
count()	returns the count of the specified item in the list
sort()	sort the list in ascending/descending order
reverse()	reverses the item of the list
copy()	returns the shallow copy of the list
"""
# =====================Using append()====================
numbers = [21, 34, 54, 12]

print("Before Append:", numbers)

# using append method
numbers.append(32)

print("After Append:", numbers)



# =====================Using extend()====================
numbers = [1, 3, 5]

even_numbers = [4, 6, 8]

# add elements of even_numbers to the numbers list
numbers.extend(even_numbers)

print("List after append:", numbers) 





# =====================Using insert()====================
numbers = [10, 30, 40]

# insert an element at index 1 (second position)
numbers.insert(1, 20)

print(numbers) # [10, 20, 30, 40]






# =====================Change List Item====================
languages = ['Python', 'Swift', 'C++']

# changing the third item to 'C'
languages[2] = 'C'

print(languages)  # ['Python', 'Swift', 'C']





# =====================Remove a item====================
languages = ['Python', 'Swift', 'C++', 'C', 'Java', 'Rust', 'R']

# deleting the second item
del languages[1]
print(languages) # ['Python', 'C++', 'C', 'Java', 'Rust', 'R']

# deleting the last item
del languages[-1]
print(languages) # ['Python', 'C++', 'C', 'Java', 'Rust']

# delete the first two items
del languages[0 : 2]  # ['C', 'Java', 'Rust']
print(languages)



# =====================Remove a item using remove()====================
languages = ['Python', 'Swift', 'C++', 'C', 'Java', 'Rust', 'R']

# remove 'Python' from the list
languages.remove('Python')

print(languages) # ['Swift', 'C++', 'C', 'Java', 'Rust', 'R']




