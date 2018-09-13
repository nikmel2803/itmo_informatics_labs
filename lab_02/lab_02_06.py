# 15
p = int(input("Введите шестнадцатеричное число на восемь разрядов: "), 16)

if p >= 0:
    print(bin(p))
else:
    p = abs(p)
    p = 4294967295 - p + 1
    print(bin(p))
