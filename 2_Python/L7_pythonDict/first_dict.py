# Python dictionary is an Ordered collection (starting from python 3.7) of items
# It stores element in keyValue pair

student = {"name": "arafat", "age": 21, "courses": ["Python", "Java", "C++"]}
print(student)
print(type(student))
# empty dictionary
user = {}
user = dict()
print(type(user))



# Accessing Dictionary
employee = {
    "name": "arafat hussain",
    "skills": ["Python", "Django", "GO"],
    "age": 21,
    "years_of_experience": 3
}
print(employee["name"])
# print(employee["salary"])         Generate an Error!

print(employee.get("skills"))
print(employee.get("salary"))       # No Error -> Return None
print(employee.get("phone", "Not found!!!"))



# Change item in Dictionary
print("---------Change in Dictionary---------")
print(employee)
"""
employee["name"] = "Arafat"
employee["years_of_experience"] = 5
print(employee["name"])
print(employee["years_of_experience"])
"""
# change multiple item at a time -> update()
employee.update(
    {
        "name": "Test User",
        "years_of_experience": 8
    }
)
print(employee)


# Add item in dictionary
print("--------Add item in dictionary----------")
person = {
    "name": "arafat",
    "age": 22,
    "profession": "student"
}
print(person)
person["nationality"] = "Bangladeshi"
print(person)
# another way
person.update(
    {
        "skills": ["Python", "JavaScript"],
        "address": "Mohakhali"
    }
)
print(person)


# Remove an item from dictionary   1. del keyword, 2. pop() method return poped item
print("--------Remove item from Dictionary----------")
del person["address"]
print(person)

print("Poped item: " + str(person.pop("skills")))
print(person)



# Copy dictionary
print("-----------Copy--------")
student_one = student
print(student_one)
student_two = student.copy()
print(student_two)

