import math


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
        for i in range(self.rowsNum):
            print("\tx{}".format(i), end="")
        out = "\t\tf("
        for i in range(self.rowsNum):
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
        out = ""
        for i in range(int(math.pow(2, self.variablesNum))):
            row = self.table.getRow(i)
            if row.value == 0:
                continue
            for j, v in enumerate(row.collection):
                out += ("¬" if v == 0 else "") + "x{}".format(j)
            out += " + "
        out = out[:-2]
        print(out)


rows = [
    Row([0, 0, 0], 0),
    Row([0, 0, 1], 0),
    Row([0, 1, 0], 1),
    Row([0, 1, 1], 0),
    Row([1, 0, 0], 1),
    Row([1, 0, 1], 1),
    Row([1, 1, 0], 1),
    Row([1, 1, 1], 1),
]

table = Table(3)

for row in rows:
    table.addRow(row)

# table.display()

f = LogicFunction(3, table)
f.getExpression()
