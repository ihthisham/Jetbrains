#Lists,Tuples and Sets

#creating list and printing
siblings = ['Naida','Fami','Ithi','Ishath']
print(siblings)

# finding length
print(len(siblings))

# accessing values using index
#indexerror - list index out of range
print(siblings[-1])

#Slicing
print(siblings[0:2])
print(siblings[2:])

#Add an item to the list
#method 1 -append()
siblings.append('New')
print(siblings)

#Method 2 -insert()
siblings.insert(0,'Elder')
print(siblings)

# Extend Method()
# bringing each individual items from 2 list
siblings_2 = ['sib1','sib2']
siblings.extend(siblings_2)
print(siblings)


#Removing item from the list

siblings.remove('sib2')
print(siblings)
popped = siblings.pop()
print(siblings)
print(popped)

#reversing the list
siblings.reverse()
print(siblings)
#Sort
siblings.sort()
print(siblings)
siblings.sort(reverse=True)
print(siblings)

#Sum
num = [1,2,3,4,5]
print(sum(num))

#Index
print(num.index(1))
# Index value error
# print(num.index(6))

#in keyword, prints true or false
print('Ithi' in siblings)

#Enumerate
# for index,siblings in enumerate(siblings,start=1):
#     print(index,siblings)

#Join Method
siblings_str = ' - '.join(siblings)
print(siblings_str)
new_list = siblings_str.split(' - ')
print(new_list)

#Tuples
#Immutable
new_tuple = ('a','b','c','d')
print (new_tuple)

#Sets
#Removes dupes
#Order of items can change/don't really care about others, mainly uses to check the membership
cs_courses = {'History','Math','Physics','Compsci','Math'}
print(cs_courses)
print('History' in cs_courses)

art_courses = {'History','Math','Art','Design'}

print(cs_courses.intersection(art_courses))
print(cs_courses.difference(art_courses))
print(cs_courses.union(art_courses))

#Empyt lists,tuples and sets
empty_set = set() #correct way
