employee = {
    "name": "Arafat Hussain",
    "age": 21,
    "skills": ["Python", "Django", "Java"],
    "address": "Mohakhali"
}
print(employee)

# .keys() method return the list of 'key' of item
print(employee.keys())
# .values() method return the list of 'value' of item
print(employee.values())
# .items() method return the list of tuple(key, value)
print(employee.items())


# Accessing through .keys() method
for current_key in employee.keys():
    print(current_key, employee[current_key])

# Accessing through .items() method
for key, value in employee.items():
    print(key, value)
