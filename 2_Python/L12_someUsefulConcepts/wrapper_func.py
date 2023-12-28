def greet(func):
    def inner():
        func()
        print("This is from inner function")
    return inner

def hello():
    print("This is from hello function")
    

print(greet(hello)())
        