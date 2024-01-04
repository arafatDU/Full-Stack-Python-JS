country_capitals = {
  "United States": "Washington D.C.", 
  "Italy": "Naples" 
}

# print dictionary keys one by one
for country in country_capitals:
    print(country)

print("----------")

# print dictionary values one by one
for country in country_capitals:
    capital = country_capitals[country]
    print(capital)
    
    
 
 
 
 
    
    
# Dictionary Membership Test
# We can check whether a key exists in a dictionary using the in operator.
my_list = {1: "Hello", "Hi": 25, "Howdy": 100}

print(1 in my_list) # True

# the not in operator checks whether key doesn't exist
print("Howdy" not in my_list) # False

print("Hello" in my_list) # False