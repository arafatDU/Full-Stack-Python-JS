countries = ["BD", "India", "UK", "USA", "China"]
print(countries[0])

# Add array item
countries.insert(4, "Uganda")
print(countries[5])

# change in array Index(0, 1, 2, 3, 4) / (-5, -4, -3, -2, -1)
countries[-1] = "Russia"
print(countries)

# Remove Array Item (del, pop(index), remove(item))
del countries[-1]
print(countries)
removed_item = countries.pop(3)
print(countries)
print("Popped item: " + removed_item)
countries.remove("UK")
print(countries)

# Accessing array with for Loop
countries_length = len(countries)
print("Length of the countries array: " + str(countries_length))
# for i in range(countries_length):
#     print(countries[i])
for i in countries:
    print(i)


