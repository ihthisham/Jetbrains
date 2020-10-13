# put your python code here
class1_students = int(input())
class2_students = int(input())
class3_students = int(input())

no_of_desks = (class1_students // 2 + class1_students % 2
               + class2_students // 2 + class2_students % 2
               + class3_students // 2 + class3_students % 2)

print(no_of_desks)