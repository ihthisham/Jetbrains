number = int(input())
i = 2
while i < number:
    print(i)
    i += 2

'''
# Good Solution
number = int(input())
if number <= 2:
    print(0)
else:
    start = 2
    while start < number:
        if start % 2 == 0:
            print(start)
        start += 1
'''