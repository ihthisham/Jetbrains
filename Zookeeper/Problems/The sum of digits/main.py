# put your python code here
number = int(input())
first_digit = number // 100
second_digit = (number // 10) % 10
third_digit = number % 10
Sum = first_digit + second_digit + third_digit
print(Sum)
