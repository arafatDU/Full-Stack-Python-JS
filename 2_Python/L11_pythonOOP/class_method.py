class Student:
    # class attributes -> represent class action
    school_name = "ABC School"

    def __init__(self, name, roll, course):
        # instance attributes -> represent instance action of an object
        self.name = name
        self.roll = roll
        self.course = course

    @classmethod    # decorator
    def get_school_name(cls):
        return cls.school_name


stu_one = Student("Arafat", 1435, "BSSE")
print(stu_one.name)

# classmethod
print(Student.get_school_name())





"""
# staticmethod
class TimeUtilityManager:

    @staticmethod
    def get_current_datetime():
        return "2023-03-21"
        
        
print(TimeUtilityManager.get_current_datetime())
"""