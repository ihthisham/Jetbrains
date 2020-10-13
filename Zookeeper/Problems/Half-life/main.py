initial = int(input())
final = int(input())
half_life = 0
while initial >= final:
    initial = initial / 2
    half_life += 1
print(half_life * 12)
