'''
Словари
'''
d1 = {
    "day": 18,
    "month": 6,
    "year": 1983
}
d2 = dict(bananas=3, apples=5, oranges=2, bag="basket")
d3 = dict([("street", "Kronverksky pr."), ("house", 49)])
d4 = dict.fromkeys(["1", "2"], 3)
print("Dict d1 = ", d1)
print("Dict d2 by dict()= ", d2)
print("Dict d3 by dict([])= ", d3)
print("Dict d4 by fromkeys = ", d4)
print("\n")

'''
Операции cо словарями
'''
d5 = d2.copy()  # создание копии словаря
print("Dict d5 copying d2 = ", d5)
# получение значения по ключу
print("Get dict value by key d5['bag']: ", d5["bag"])
print("Get dict value by key d5.get('bag'): ", d5.get('bag'))
print("Get dict keys d5.keys(): ", d5.keys())  # список ключей
print("Get dict values d5.values(): ", d5.values())  # список значений
print("\n")

myInfo = {
    "surname": "Мельников",
    "name": "Никита",
    "middlename": "Павлович",
    "day": "28",
    "month": "Март",
    "year": "2000",
    "university": "ИТМО"
}
print("Get dict keys myInfo.keys(): ", myInfo.keys())
print("Get dict values myInfo.values(): ", myInfo.values())
