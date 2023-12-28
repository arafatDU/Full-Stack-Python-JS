def zero_divide_error(func):
    def inner(a, b):
        if(b == 0):
            return "Zero Divisible Error"
        
        return func(a, b)
    return inner 


@zero_divide_error
def divide(a, b):
    return a/b

print(divide(10, 2))
print(divide(10, 4))
print(divide(10, 0))