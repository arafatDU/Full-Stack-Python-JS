# fibonacci 0 1 1 2 3 5 8 13 ..........
def fibonacci(n):
    if n == 0:
        return 0
    else:
        x = 0
        y = 1
        print(x)
        print(y)
        for i in range(n):
            z = x + y
            x = y
            y = z
            print(z)


fibonacci(4)
