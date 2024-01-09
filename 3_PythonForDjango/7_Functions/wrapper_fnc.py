# Wrapper function

def myWrapper(fn):
    def test():
        print("I am from test, before")
        fn()
        print("I am from test, after")
    return test


def greet():
    print("I am greet function, before")
    
greet = myWrapper(greet)
greet()