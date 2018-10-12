import math
from textwrap import wrap


# Дарова народ
# Кароч тут куча говнокода
# Если почувствуете жжение в глазах, огонь в пукане - рекомендуется закрыть страницу
# Лучше сначала прочитать эту статью и всё понять: https://ru.wikipedia.org/wiki/Метод_Куайна_—_Мак-Класки
class Row:
    count = 0

    def __init__(self, collection, value):
        self.id = Row.count
        Row.count += 1
        self.collection = collection
        self.value = value


class Table:
    def __init__(self, rowsNum):
        self.rowsNum = rowsNum
        self.rows = []

    def addRow(self, row):
        for r in self.rows:
            if r.id == row.id:
                print("ERROR!")
                return
        self.rows.append(row)

    def setRow(self, row):
        for i, r in enumerate(self.rows):
            if r.id != row.id:
                continue
            self.rows[i] = row
            return
        print("ERROR")

    def getRow(self, rowId):
        for r in self.rows:
            if r.id == rowId:
                return r

    def display(self):
        print("id", end="")
        for i in range(int(math.sqrt(self.rowsNum))):
            print("\tx{}".format(i), end="")
        out = "\t\tf("
        for i in range(int(math.sqrt(self.rowsNum))):
            out += "x{},".format(i)
        out = out[:-1] + ")"
        print(out)
        for i, r in enumerate(self.rows):
            out = str(i)
            for v in r.collection:
                out += "\t{}".format(v)
            out += "    |    " + str(r.value)
            print(out)


class LogicFunction:
    def __init__(self, variablesNum, table):
        self.variablesNum = variablesNum
        self.table = table

    def getTable(self):
        return self.table

    def printTable(self):
        table.display()

    def getExpression(self):
        # Решил инкапсулировать некоторый код в функции для лучшего восприятия кода
        # Внизу сначала объявлено несколько вспомогальных функций

        # Функция считает дистанцию Хемминга аргументов a и b
        def hamming_distance(a, b):
            d = 0
            for i in range(len(a)):
                if a[i] != b[i]:
                    d += 1
            return d

        # Делает следующую хрень:
        # допустим, a = 0011, b = 0001
        # тогда на выходе будет строка 00-1
        def combine(a, b):
            result = []
            for i in range(len(a)):
                if a[i] != b[i]:
                    result.append("-")
                    continue
                result.append(a[i])
            return "".join(result)

        # Кароч эта функция возращает список импликантов
        # см. https://ru.wikipedia.org/wiki/Метод_Куайна_—_Мак-Класки, Шаг 1
        # Тут рекурсия
        def return_impl(mint):
            result = []
            is_final = 0
            for i in range(len(mint) - 1):
                combineCount = 0
                for j in range(len(mint)):
                    if hamming_distance(mint[i], mint[j]) == 1:
                        combine_result = combine(mint[i], mint[j])
                        combineCount += 1
                        is_final += 1
                        if combine_result in result:
                            continue
                        result.append(combine_result)
                if combineCount == 0:
                    result.append(mint[i])
            if not is_final:
                result.append(mint[-1])
                return result
            return return_impl(result)

        # Начало реализации шага 1 из вышеприведённой статьи

        collections = []  # список значений таблицы истинности, при которых функция истинна
        rows_num = int(math.pow(2, self.variablesNum))
        for item in range(rows_num):
            row = self.table.getRow(item)
            if row.value == 0:
                continue
            collections.append(''.join(str(x) for x in row.collection))

        # из полученной колекции получаем список импликантов
        impl = return_impl(collections)
        print("collections: ", collections)
        print("impl: ", impl)

        # Конец реализации первого шага

        # Вспомогательные функции для второго шага

        # Функция для удаления колонок из таблицы table, у которых на строке index_horiz стоит 1
        # Тут рекурсия
        def delete_columnes(table, index_horiz, index_vertical=0):
            if sum(table[index_horiz]) == 0:
                return
            if table[index_horiz][index_vertical] == 1:
                for j in range(len(table)):
                    del table[j][index_vertical]
                delete_columnes(table, index_horiz, index_vertical)
            else:
                delete_columnes(table, index_horiz, index_vertical + 1)

        # Проверка соответствия b к a
        # Другими словами: если a = 0011, а b = 00-1,
        # то функция вернёт True (вместо "-" можно подставить 1 и получится a)
        def match(a, b):
            result = True
            for i in range(len(a)):
                if b[i] == "-":
                    continue
                if b[i] != a[i]:
                    result = False
            return result

        # Подсчёт суммы элементов колонки
        def column_sum(table, colIndex):
            summa = 0
            index = 0
            for j in range(len(table)):
                summa += table[j][colIndex]
                if table[j][colIndex] == 1:
                    index = j
            return summa, index

        # Ищет на какой строке сумма элементов максимальна
        # Возращает номер такой строки
        def max_line_sum(table):
            max = 0
            max_index = 0
            for i in range(len(table)):
                summa = sum(table[i])
                if summa > max:
                    max = summa
                    max_index = i
            return max_index

        # Работаем с таблицей простых импликант
        # Это основная функция шага 2
        # Тут рекурсия
        def table_pars(table, impl):
            output = ""
            for i in range(len(table[0])):
                summa, index = column_sum(table, i)
                if summa == 1:
                    delete_columnes(table, index)
                    del table[index]
                    output += impl.pop(index)
                    break
                else:
                    index = max_line_sum(table)
                    delete_columnes(table, index)
                    del table[index]
                    output += impl.pop(index)
                    break

            if len(table) == 0 or len(table[0]) == 0:
                return output
            output += table_pars(table, impl)
            return output

        # Начало реализации шага 2
        table = []
        for j in range(len(impl)):
            table.append([])
            for item in range(len(collections)):
                table[j].append(1 if match(collections[item], impl[j]) else 0)
        print("table: ", table)
        output = table_pars(table, impl)
        # Конец реализации шага 2

        # Ну а сейчас осталось только привести в функцию в человеческий вид :)
        output_list = wrap(output, self.variablesNum)
        result = ""
        for i in output_list:
            for index, j in enumerate(i):
                if j == "1":
                    result += "x{}".format(index)
                if j == "0":
                    result += "¬x{}".format(index)
            result += " + "
        result = result[:-2]
        return result


# путём комментирования\расскоментирования нужных строк
# можно протестить прогу на разных входных значениях


# rows = [
#     Row([0, 0, 0], 0),
#     Row([0, 0, 1], 0),
#     Row([0, 1, 0], 1),
#     Row([0, 1, 1], 0),
#     Row([1, 0, 0], 1),
#     Row([1, 0, 1], 1),
#     Row([1, 1, 0], 1),
#     Row([1, 1, 1], 1)
# ]

# rows = [
#     Row([0], 1),
#     Row([1], 0)
# ]


# rows = [
#     Row([0, 0], 1),
#     Row([0, 1], 0),
#     Row([1, 0], 0),
#     Row([1, 1], 1),
# ]

# rows = [
#     Row([0, 0, 0, 0], 0),
#     Row([0, 0, 0, 1], 0),
#     Row([0, 0, 1, 0], 1),
#     Row([0, 0, 1, 1], 1),
#     Row([0, 1, 0, 0], 0),
#     Row([0, 1, 0, 1], 0),
#     Row([0, 1, 1, 0], 0),
#     Row([0, 1, 1, 1], 0),
#     Row([1, 0, 0, 0], 1),
#     Row([1, 0, 0, 1], 1),
#     Row([1, 0, 1, 0], 1),
#     Row([1, 0, 1, 1], 0),
#     Row([1, 1, 0, 0], 0),
#     Row([1, 1, 0, 1], 1),
#     Row([1, 1, 1, 0], 0),
#     Row([1, 1, 1, 1], 1)
# ]
# rows = [
#     Row([0, 0, 0, 0], 0),
#     Row([0, 0, 0, 1], 0),
#     Row([0, 0, 1, 0], 0),
#     Row([0, 0, 1, 1], 0),
#     Row([0, 1, 0, 0], 1),
#     Row([0, 1, 0, 1], 0),
#     Row([0, 1, 1, 0], 0),
#     Row([0, 1, 1, 1], 0),
#     Row([1, 0, 0, 0], 1),
#     Row([1, 0, 0, 1], 1),
#     Row([1, 0, 1, 0], 1),
#     Row([1, 0, 1, 1], 1),
#     Row([1, 1, 0, 0], 1),
#     Row([1, 1, 0, 1], 0),
#     Row([1, 1, 1, 0], 1),
#     Row([1, 1, 1, 1], 1)
# ]
rows = [
    Row([0, 0, 0, 0], 0),
    Row([0, 0, 0, 1], 0),
    Row([0, 0, 1, 0], 0),
    Row([0, 0, 1, 1], 0),
    Row([0, 1, 0, 0], 0),
    Row([0, 1, 0, 1], 0),
    Row([0, 1, 1, 0], 0),
    Row([0, 1, 1, 1], 0),
    Row([1, 0, 0, 0], 0),
    Row([1, 0, 0, 1], 0),
    Row([1, 0, 1, 0], 0),
    Row([1, 0, 1, 1], 0),
    Row([1, 1, 0, 0], 0),
    Row([1, 1, 0, 1], 0),
    Row([1, 1, 1, 0], 0),
    Row([1, 1, 1, 1], 1)
]

table = Table(len(rows))

for row in rows:
    table.addRow(row)

# table.display()

f = LogicFunction(int(math.log2(len(rows))), table)
print(f.getExpression())
