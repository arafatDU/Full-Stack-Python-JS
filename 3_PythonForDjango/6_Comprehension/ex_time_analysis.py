# Import required module 
import time 


# define function to implement for loop 
def for_loop(n): 
	result = [] 
	for i in range(n): 
		result.append(i**2) 
	return result 


# define function to implement list comprehension 
def list_comprehension(n): 
	return [i**2 for i in range(n)] 


# Driver Code 

# Calculate time taken by for_loop() 
begin = time.time() 
for_loop(10**6) 
end = time.time() 

# Display time taken by for_loop() 
print('Time taken for_loop:', round(end-begin, 2)) 

# Calculate time takens by list_comprehension() 
begin = time.time() 
list_comprehension(10**6) 
end = time.time() 

# Display time taken by for_loop() 
print('Time taken for list_comprehension:', round(end-begin, 2)) 
