# put your python code here
hour1 = int(input())
# print()
minute1 = int(input())
# print()
second1 = int(input())
# print()
hour2 = int(input())
# print()
minute2 = int(input())
# print()
second2 = int(input())
# print()

no_of_seconds1 = (hour1 * 60 * 60) + (minute1 * 60) + second1
no_of_seconds2 = (hour2 * 60 * 60) + (minute2 * 60) + second2

print(abs(no_of_seconds1 - no_of_seconds2))
