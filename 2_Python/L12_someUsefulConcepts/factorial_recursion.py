# 5! = 1 * 2 * 3 * 4 * 5

def factorial(n):
    if n == 1:
        return 1
    m = factorial(n-1)
    return n * m


f = factorial(5)
print(f)
