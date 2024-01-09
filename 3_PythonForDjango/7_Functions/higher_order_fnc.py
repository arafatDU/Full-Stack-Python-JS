# Higher Order Function
def hof(fn):
    print(fn.__name__)
    fn()
    

def greet():
    print("Hello World")
    
    
def hello():
    print("Hello Bohubrihi")
    

hof(greet)




# Higher Order Function -> return function
def myFunction():
    def hello2():
        print("Hello Arafat")
        
    return hello2

f = myFunction()
f()



li = [1, 2, 3, 4, 5, 6]

newL = list(filter(lambda x: x%2==1, li))
print(newL)