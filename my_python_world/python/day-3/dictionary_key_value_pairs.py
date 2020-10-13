'''Dictionary or Key Value pairs
or Hash Map or Associative array'''

student = {'name':'John','age': 25,'courses':['Math','Compsci']}
# print(student)

print(student['age'])
print(student.get('phone','Not Found'))

# student['phone'] = '555-5555'
# student['name'] = 'Jane'
# print(student)

#Update method
student.update({'name' : 'Umer','age' : 29,'courses': ['Statistics','Math','Programming'],'phone': '9995239983'})
print(student)

#Deleting Item

# del student ['age']

# age = student.pop('age')
# print(age)
# print(student)

#Retrieving keys and values
print(student.keys())
print(student.values())
print(student.items())

# looping through the dicts

# for key in student:
#     print(key)

for key,value in student.items():
    print(key,value)