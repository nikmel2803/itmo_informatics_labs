# 14

from itertools import permutations

s = input("Введите строку")
a = set()
for item in permutations(s):
    a.add(''.join(item))
print('\n'.join(a))
