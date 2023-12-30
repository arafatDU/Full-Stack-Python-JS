subject = "Software Engineering"
student_name = ["Arafat", "Adnan", "Hasin", "Rakib", "Zisun"]
student_roll = [1401, 1402, 1403, 1404, 1405]
cse101_marks = [75, 80, 78, 90, 69]
cse102_marks = [81, 71, 80, 61, 78]
se106_marks = [86, 66, 76, 67, 64]
credit = {
    'CSE101': 3,
    'CSE102': 3,
    'SE106': 3
}


def mark_to_grade(mark):
    if 80 <= mark <= 100:
        return 4.00
    elif 75 <= mark < 80:
        return 3.75
    elif 70 <= mark < 75:
        return 3.50
    elif 65 <= mark < 70:
        return 3.25
    elif 60 <= mark < 65:
        return 3.00
    elif 55 <= mark < 60:
        return 2.75
    elif 50 <= mark < 55:
        return 2.50
    elif 45 <= mark < 50:
        return 2.25
    elif 40 <= mark < 45:
        return 2.00
    elif 0 <= mark < 40:
        return 0
    else:
        return -1


def marks_to_gradelist(marks, gradelist):
    for mark in marks:
        gradelist.append(mark_to_grade(mark))


def sum_of_grade_multiply_credit(gradelist, creditlist):
    sum_of_prod = 0
    for k in range(len(gradelist)):
        if gradelist[k] == 0:
            return 0
        sum_of_prod += gradelist[k] * creditlist[k]
    return round(sum_of_prod, 2)


def grade_to_letter(grade):
    if grade == 4.00:
        return 'A+'
    elif grade == 3.75:
        return 'A'
    elif grade == 3.50:
        return 'A-'
    elif grade == 3.25:
        return 'B+'
    elif grade == 3.00:
        return 'B'
    elif grade == 2.75:
        return 'B-'
    elif grade == 2.50:
        return 'C+'
    elif grade == 2.25:
        return 'C'
    elif grade == 2.00:
        return 'C-'
    else:
        return 'F'



credit_list = list(credit.values())
course_list = list(credit.keys())
total_credit = sum(credit_list)
# print(total_credit)
cse101_grade = []
cse102_grade = []
se106_grade = []
gpa = []

marks_to_gradelist(cse101_marks, cse101_grade)
marks_to_gradelist(cse102_marks, cse102_grade)
marks_to_gradelist(se106_marks, se106_grade)

for i in range(len(student_roll)):
    grade_list_of_each_student = [cse101_grade[i], cse102_grade[i], se106_grade[i]]
    # print(grade_list_of_each_student)
    sum_of_product = sum_of_grade_multiply_credit(grade_list_of_each_student, credit_list)
    gpa.append(round(sum_of_product / total_credit, 2))

# print(se106_grade)
# print(cse101_grade)
# print(cse102_grade)
# print(gpa)

print("============================================================================")
print("-----------------------------------Result-----------------------------------")
print("============================================================================\n")
print("What do you want to see?")
print("                1. All Result\n                2. Individual Result\n")
choice = int(input("Enter your choice: "))

if choice == 1:
    with open('result.txt', 'w') as file:
        file.write("Roll        Name           GPA\n===============================\n")
    for i in range(len(student_roll)):
        with open('result.txt', 'a') as file:
            file.write("{}        {}     {}\n".format(student_roll[i], student_name[i].ljust(10, ' '), gpa[i]))
    print("Result updated successfully in result.txt")


elif choice == 2:
    print("---------------Individual Result Panel----------------")
    stu_roll = int(input("Enter your roll: "))
    if stu_roll in student_roll:
        index = student_roll.index(stu_roll)
        with open('result_of_{}.txt'.format(stu_roll), 'w') as file:
            file.write("========================================================================\n")
            file.write("                Result of BSSE 1st Year 1st Semester\n")
            file.write("========================================================================\n\n\n")
            file.write("                           {}\n\nRoll: {}\n".format(student_name[index], stu_roll))
            file.write("Subject: {}\nGrade: {}\n".format(subject, gpa[index]))
            file.write("Result: {}\n\n".format("Promoted" if gpa[index] > 0 else "Failed"))
            file.write("_______________________________Mark Sheet_______________________________\n")
            for i in range(len(course_list)):
                grade_list = [cse101_grade[index], cse102_grade[index], se106_grade[index]]
                file.write("{}         {}         {}          {}\n".format(course_list[i].ljust(10, ' '),
                                                                           grade_list[i],
                                                                           grade_to_letter(grade_list[i]),
                                                                           credit_list[i]))

        print("Result updated successfully in result_of_{}.txt".format(stu_roll))


    else:
        print("Your roll is not found!")

else:
    print("Invalid input")
