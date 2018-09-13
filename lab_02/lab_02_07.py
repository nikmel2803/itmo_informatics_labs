# 16

p = int(input("Введите двенадцатеричное число: "), 12)

positive = p >= 0
p = abs(p)
n = ""
while p > 0:
    y = str(p % 14)
    if y == "10":
        y = "A"
    elif y == "11":
        y = "B"
    elif y == "12":
        y = "C"
    elif y == "13":
        y = "D"
    n = y + n
    p = int(p / 14)
if n == "":
    n = "0"
if not positive:
    n = "-" + n
print(n)
