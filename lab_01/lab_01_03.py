'''     Форматированный ввод/вывод данных '''
m = 10
pi = 3.1415927
print("m = ", m)
print("m = %d" % m)
print("%7d" % m)
print("pi = ", pi)
print("%.3f" % pi)
print("%10.4f\n" % pi)
print("m = {}, pi = {}".format(m, pi))
ch = 'A'
print("ch = %c" % ch)
s = "Hello"
print("s = %s" % s)
print("\n\n")

code = input("Enter your position number in group: ")
n1, n2 = input("Enter two numbers splitted by space: ").split()
d, m, y = input("Enter three numbers splitted by \'.\': ").split('.')
print("{} + {} = {}".format(n1, n2, float(n1) + float(n2)))
print("Your birthday is %s.%s.%s and you are %d in the group list" % (d, m, y, int(code)))

# 16, 17
print("\n\n")
print("m = %4d; pi = %.3f" % (int(m), pi))
print("m = {}; pi = {}".format(m, pi))

# 18
print("\n\n")
year = int(input("Введите курс обучения"))
print("Ваш курс обучение: ", year)

# 19
r1, m1, p1 = input("Введите ваши баллы по русскому языку, математике и информатике через запятую").split(",")
print("Ваши баллы: русский язык {}, математика {}, информатика {}".format(r1, m1, p1))

print("\n\n")
# 20
print(int(input("Введите двенадцатиразрядное число: "), int(input("Введите ваше день рождения: ")) % 8 + 2))

# 21
print("\n\n")
n = int(input("Введите число"))
print("n>>1 = ", n >> 1)
print("n<<1 = ", n << 1)
