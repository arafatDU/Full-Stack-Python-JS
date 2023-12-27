class Person:

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        return "My name is {}".format(self.name)


class Student(Person):

    def __init__(self, name, age, gender, course):
        self.course = course
        Person.__init__(self, name, age, gender)


stu_one = Student("Arafat", 21, "Male", ["C", "C++"])
print(stu_one.introduce())
