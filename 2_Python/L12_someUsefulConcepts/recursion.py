# printing numbers from 1 to 10 by recursion
def print_numbers(n):
    if n > 10:
        return
    print(n)
    print_numbers(n + 1)


print_numbers(5)

