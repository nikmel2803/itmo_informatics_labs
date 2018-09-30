class Encoder:
    def __init__(self):
        self.__compressionCoef = 0

    def encode(self, str):
        return str

    def decode(self, str):
        return str

    def setCompressionCoef(self, val):
        self.__compressionCoef = val

    def getCompressionCoef(self):
        return self.__compressionCoef


class HuffmanEncoder(Encoder):
    def __init__(self):
        Encoder.__init__(self)

    def __huffman(self, p):
        """Возвращает словарь вида: символ - код символа"""
        # Если всего два элемента во входном словаре, то первому присваивается код 0, а второму 1
        if len(p) == 1:
            return dict(zip(p.keys(), ['0']))
        if len(p) == 2:
            return dict(zip(p.keys(), ['0', '1']))
        # Соединяем два элемента во входном словаре с наименьшими вероятностями
        pCopy = p.copy()
        a1, a2 = self.__lowestProbabilitiesPair(p)
        p1, p2 = pCopy.pop(a1), pCopy.pop(a2)
        pCopy[a1 + a2] = p1 + p2

        # Рекурсия
        c = self.__huffman(pCopy)
        ca1a2 = c.pop(a1 + a2)
        c[a1], c[a2] = ca1a2 + '0', ca1a2 + '1'
        return c

    def __lowestProbabilitiesPair(self, p):
        """Возращает символы наименьшей вероятностью"""

        # Сортирует словарь (символы с наименьшей вероятностью оказываются в начале
        sortedP = sorted(p.items(), key=lambda i: i[1])
        return sortedP[0][0], sortedP[1][0]

    def encode(self, string):
        frequencyDic = {}  # символ - частота встречаемости
        charCount = 0  # количество символов в файле
        for char in string:
            charCount += 1
            if char in frequencyDic.keys():
                frequencyDic[char] += 1
            else:
                frequencyDic[char] = 1

        for key in frequencyDic:
            frequencyDic[key] = frequencyDic[key] / charCount
        codes = self.__huffman(frequencyDic)
        result = ""
        for key in codes:
            val = str(key)
            if key == '\n':  # костыль для нормального кодирования переноса строки
                val = "\\n"
            result += val + "+" + codes[key] + "\n"
        for char in string:
            result += codes[char]

        self.setCompressionCoef(len(result) / len(string))
        return result

    def decode(self, string):
        codes = {}
        lines = string.split("\n")
        for line in range(0, len(lines) - 1):
            code = lines[line].split("+")
            codes[code[1].replace("\n", "")] = code[0]
        encode = lines.pop()
        tmp = ""
        result = ""
        for char in encode:
            tmp += char
            if codes.get(tmp) is None:
                continue
            if codes[tmp] == "\\n":  # костыль для нормального декодирования переноса строки
                codes[tmp] = "\n"
            result += codes[tmp]
            tmp = ""
        return result


class LZEncoder(Encoder):
    def __init__(self):
        Encoder.__init__(self)

    def encode(self, string):
        code = ""
        dict = {}
        tmp = ""
        index = 1
        for i in range(0, len(string)):
            tmp += string[i]
            if tmp not in dict:
                if len(tmp) == 1:
                    code = code + "0," + tmp + "_"
                    dict[tmp] = index
                    index += 1
                    tmp = ""
                    continue
                else:
                    code = code + str(dict.get(tmp[0:len(tmp) - 1])) + "," + string[i] + "_"
                    dict[tmp] = index
                    index += 1
                    tmp = ""
                    continue
            if i == len(string) - 1:
                code = code + str(dict.get(tmp)) + "," + "&"
        return code

    def decode(self, code):
        s = code.split("_")
        if "" in s:
            s.remove("")
        index = 1
        dictionary = {}
        string = ""
        for item in s:
            i = item[0:item.find(",")]
            c = item[item.find(",") + 1:]
            if c == "&":
                c = ""
            if i == "0":
                string += c
                dictionary[str(index)] = c
                index += 1
                continue
            string = string + dictionary[str(i)] + c
            dictionary[str(index)] = dictionary[str(i)] + c
            index += 1
        self.setCompressionCoef(len(string) / len(code))
        return string


# huff = HuffmanEncoder()
# print(huff.decode(huff.encode("Python is a widely used high-level programming language for general-purpose programming, created by Guido van Rossum and first released in 1991.")))

lz = LZEncoder()
print(lz.decode(lz.encode(
    "Python is a widely used high-level programming language for general-purpose programming, created by Guido van Rossum and first released in 1991.")))
