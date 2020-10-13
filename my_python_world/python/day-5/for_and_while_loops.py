# for and while loop

nums = [1,2,3,4,5]

# for with if,continue and break
for num in nums:
    if num == 4:
        print('found')
        continue #break
    print(num)

# double loop creates the combin    ation
for num in nums:
    for letter in 'abc':
        print(num,letter)

# range method
for i in range(1,11):
    print(i)

# While loop
x = 0

while True: #True - for infinite loop, control C for interrupting the infinite loop
    if x==5:
        break
    print(x)
    x+=1
