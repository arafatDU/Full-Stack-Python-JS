# Keyword Argument Function
def hello(fname="arafat", lname="hussain"):
    print(f"Hello {fname} {lname}")
    
hello()



# Arbitary Keyword Argument--- must pass key
def fun1(**kwargs):
    print(kwargs)
    print(kwargs['fname'])
    
fun1(fname="Arafat", lname="Hussain", age=21)




def fun2(*args, **kwargs):
    print(args)
    print(kwargs)
    

fun2("arafat", 21, True, fname="Arafat", age=21)
fun2("arafat", 21, True)
fun2()