# creating a dictionary
country_capitals = {
  "United States": "Washington D.C.", 
  "Italy": "Rome", 
  "England": "London"
}

# printing the dictionary
print(country_capitals)




# Valid dictionary

my_dict = {
  1: "Hello", 
  (1, 2): "Hello Hi", 
  3: [1, 2, 3]
}

print(my_dict)

# Invalid dictionary
# Error: using a list as a key is not allowed

my_dict = {
  1: "Hello", 
  [1, 2]: "Hello Hi", 
}

print(my_dict)





# Python Dictionary Length
country_capitals = {
  "United States": "Washington D.C.", 
  "Italy": "Rome", 
  "England": "London"
}

# get dictionary's length
print(len(country_capitals)) # 3




# Access Dictionary Items
country_capitals = {
  "United States": "Washington D.C.", 
  "Italy": "Rome", 
  "England": "London"
}

print(country_capitals["United States"])  # Washington D.C.

print(country_capitals["England"]) # London





# Change Dictionary Items
country_capitals = {
  "United States": "Washington D.C.", 
  "Italy": "Naples", 
  "England": "London"
}

# change the value of "Italy" key to "Rome"
country_capitals["Italy"] = "Rome"

print(country_capitals)





# Add Items to a Dictionary
country_capitals = {
  "United States": "Washington D.C.", 
  "Italy": "Naples" 
}

# add an item with "Germany" as key and "Berlin" as its value
country_capitals["Germany"] = "Berlin"

print(country_capitals)





# Remove Dictionary Items
country_capitals = {
  "United States": "Washington D.C.", 
  "Italy": "Naples" 
}

# delete item having "United States" key
del country_capitals["United States"]


print(country_capitals)




# Remove all items from the dictionary at once
country_capitals = {
  "United States": "Washington D.C.", 
  "Italy": "Naples" 
}

country_capitals.clear()

print(country_capitals) # {}




'''
Python Dictionary Methods
Here are some of the commonly used dictionary methods.

Function	Description
pop()	    Remove the item with the specified key.
update()	Add or change dictionary items.
clear()	    Remove all the items from the dictionary.
keys()	    Returns all the dictionary's keys.
values()	Returns all the dictionary's values.
get()	    Returns the value of the specified key.
popitem()	Returns the last inserted key and value as a tuple.
copy()	    Returns a copy of the dictionary.
'''