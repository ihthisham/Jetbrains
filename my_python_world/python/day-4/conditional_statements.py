# if,elif and else: Checks the conditions and evaluates to True or False

a=5
b=8

if a>b:
    print('a is greater than b')
else:
    print('b is greater')

# elif
language = 'C'

if language == 'Python':
    print('Language is python')
elif language == 'Java':
    print('Language is Java')
else:
    print('no match')

# and,or, not

user = 'Admin'
logged_in = True

if user == 'Admin' or logged_in:
    print('Admin Page')
else:
    print('Bad Creds')

if not logged_in:
    print('Please log in')
else:
    print('Welcome')

# is,id

l1 = [1,2,3]
l2 = [1,2,3]

print (l1==l2)
print(l1 is l2)
print(id(l1)==id(l2))


l3 = [1,2,3]
l4 = l3

print (l3==l4)
print(l3 is l4)
print(id(l1))
print(id(l2))
print(id(l3))
print(id(l4))

# False Values:
    # False
    # None
    # Zero of any numeric type
    # Any empty sequence. For example, '', (), [].
    # Any empty mapping. For example, {}.

condition = {}

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

