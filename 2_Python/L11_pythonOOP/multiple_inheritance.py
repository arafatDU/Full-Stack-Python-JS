# called Diamond Problem

class A:

    def __init__(self):
        print("From Class A")


class B:

    def __init__(self):
        print("From Class B")



class C(A, B):

    def __init__(self):
        print("From Class C")
        A.__init__(self)
        B.__init__(self)  # need to individual class ---- Better approach = super function



obj_c = C()
