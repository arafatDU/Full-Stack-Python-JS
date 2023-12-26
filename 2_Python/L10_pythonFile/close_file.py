"""
file = open('test_file.txt', 'r')
print(file.read())
file.close()
"""

# Better way
with open('test_file.txt', 'r') as file:
    print(file.read())
