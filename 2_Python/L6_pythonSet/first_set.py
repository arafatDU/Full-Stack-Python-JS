# Sets are unordered
# Set elements are unique. Duplicate elements are not allowed
# A set itself may be modified, but the element contain in the set must be of an immutable type (X List)

fruits = {"mango", "apple", "banana", "apple", "mango"}
print(fruits)
print(type(fruits))

# set() constractor
fruits = set(["mango", "apple", "banana", "apple", "mango"])
print(fruits)
print(type(fruits))

# fruit = {}       this is from 'dict' class, not 'set'
fruit = set()
print(type(fruit))


# Check a item is present or not in Set
print("mango" in fruits)
print("amm" in fruits)

# Add item to set
user_name = {"arafat", "hussain"}
print(user_name)
user_name.add("test")
user_name.add("john")
user_name.add((1, 2))        # Adding Tuple (List can't be added)
print(user_name)


# Remove an item from set
user_name.remove("test")
print(user_name)

user_name.discard("hussain")
user_name.discard("Hello")     # Don't generate error
print(user_name)


# Loop on set
for current_user in user_name:
    print(current_user)       # Don't maintain order!

