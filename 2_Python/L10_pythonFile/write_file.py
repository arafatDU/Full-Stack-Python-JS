"""
with open('test_file.txt', 'w') as file:
    file.write("This is from our program. ")
"""

with open('test_file.txt', 'a') as file:
    all_list = ["This is a test 1\n", "This a test 2\n", "This is a test 3\n"]
    file.write("This is from our program.\n")
    file.writelines(all_list)

