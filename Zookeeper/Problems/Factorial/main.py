number = int(input())
i = 1
factorial = 1
while i < number:
    factorial += factorial * i
    i += 1
print(factorial)
