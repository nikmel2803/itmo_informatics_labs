# 14

from itertools import permutations

s = input("Введите строку")

for item in permutations(s):
    print(''.join(item))
