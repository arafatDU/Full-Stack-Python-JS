class Person:

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        return "My name is {}".format(self.name)



user_one = Person("Arafat", 21, "Male")
user_two = Person("Sakib", 20, "Male")

print(user_one.name)
print(user_one.age)
print(user_one.gender)

print(user_two.name)
print(user_two.age)
print(user_two.gender)

# print(user_one)
# print(type(user_one))

print(user_one.introduce())
