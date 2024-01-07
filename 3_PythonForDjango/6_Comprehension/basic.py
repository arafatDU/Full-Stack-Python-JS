numbers = [12, 13, 14,] 
doubled = [x *2 for x in numbers] 
print(doubled)



numbers = [1, 2, 3, 4, 5] 
squared = [x ** 2 for x in numbers] 
print(squared)



# Using list comprehension to iterate through loop 
List = [character for character in [1, 2, 3]] 

# Displaying list 
print(List)


list = [i for i in range(11) if i % 2 == 0] 
print(list)





matrix = [[j for j in range(3)] for i in range(3)] 
	
print(matrix)
# Output: [[0, 1, 2], [0, 1, 2], [0, 1, 2]]



