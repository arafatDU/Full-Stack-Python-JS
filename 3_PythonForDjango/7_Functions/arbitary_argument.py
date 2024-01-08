# normal function with positional argument
def greet(fname, lname):
    print(f"Hello {fname} {lname}")
    
greet("Arafat", "Hussain")


# Function with arbitary argument-> get Tuple
def test(*args):
    print(args)
    
test("arafat", 21, True)






# WITHOUT ARBITRARY ARGUMENT

list_to_sum = [1,2,3,4,5]

def sum_function(numbers):
    total = 0
    for i in numbers:
        total += i

    return total

print(sum_function(list_to_sum))




# WITH ARBITRARY ARGUMENT

def sum_function(*numbers):
    total = 0
    for i in numbers:
        total += i

    return total
    
print(sum_function(1,2,3,4,5))