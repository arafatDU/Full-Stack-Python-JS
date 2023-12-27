"""
A
B -> A
C -> B -> A  #multi_level_inheritance

    _C-> B -> A
D                   #Diamond Problem  -> super()  D -> C -> B -> A   #Python_vizualation_method
    _B -> A
"""


class A:

    def __init__(self):
        print("From Class A")


class B(A):

    def __init__(self):
        print("From Class B")
        # A.__init__(self)
        super().__init__()
        

class C(B):

    def __init__(self):
        print("From Class C")
        # B.__init__(self)
        super().__init__()


    def my_method(self):
        print("This is from class C")


class D(C, B):

    def __init__(self):
        print("From Class D")
        # C.__init__(self)
        # B.__init__(self)
        super().__init__()


obj_d = D()
