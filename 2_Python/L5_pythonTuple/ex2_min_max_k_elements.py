"""
Sometimes, while dealing with tuples, we can have problem in which
we need to extract only extreme K elements, i.e maximum and minimum K elements in Tuple.
This problem can have applications across domains such as web development and Data Science.
Let’s discuss certain ways in which this problem can be solved.

Input : test_tup = (3, 7, 1, 18, 9), k = 2
Output : (3, 1, 9, 18)

Input : test_tup = (3, 7, 1), k=1
Output : (1, 7)
"""

test_tuple = (5, 20, 3, 7, 6, 8)
k = 2
print("The original Tuple: " + str(test_tuple))

test_tuple = list(sorted(test_tuple))
result = []

for index, val in enumerate(test_tuple):        # test_tuple must enumerate()
    if index < k or index >= len(test_tuple) - k:
        result.append(val)

result = tuple(result)
print("The Extracted values: " + str(result))

