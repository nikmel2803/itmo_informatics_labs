# 25

def huffman(p):
    """Возвращает словарь вида: символ - код символа"""
    # Если всего два элемента во входном словаре, то первому присваивается код 0, а второму 1
    if len(p) == 2:
        return dict(zip(p.keys(), ['0', '1']))

    # Соединяем два элемента во входном словаре с наименьшими вероятностями
    pCopy = p.copy()
    a1, a2 = lowestProbabilitiesPair(p)
    p1, p2 = pCopy.pop(a1), pCopy.pop(a2)
    pCopy[a1 + a2] = p1 + p2

    # Рекурсия
    c = huffman(pCopy)
    ca1a2 = c.pop(a1 + a2)
    c[a1], c[a2] = ca1a2 + '0', ca1a2 + '1'

    return c


def lowestProbabilitiesPair(p):
    """Возращает символы наименьшей вероятностью"""

    # Сортирует словарь (символы с наименьшей вероятностью оказываются в начале
    sortedP = sorted(p.items(), key=lambda i: i[1])
    return sortedP[0][0], sortedP[1][0]


def encodeHuffman(fileIn, fileOut):
    try:
        frequencyDic = {}  # символ - частота встречаемости
        inputFile = open(fileIn, 'r')
        charCount = 0  # количество символов в файле
        for line in inputFile:
            for char in line:
                charCount += 1
                if char in frequencyDic.keys():
                    frequencyDic[char] += 1
                else:
                    frequencyDic[char] = 1
        inputFile.close()
        for key in frequencyDic:
            frequencyDic[key] = frequencyDic[key] / charCount
        codes = huffman(frequencyDic)
        inputFile = open(fileIn, 'r')
        outputFile = open(fileOut, "w")
        for key in codes:
            val = str(key)
            if key == '\n':  # костыль для нормального кодирования переноса строки
                val = "\\n"
            outputFile.write(val + "+" + codes[key] + "\n")
        for line in inputFile:
            for char in line:
                outputFile.write(codes[char])
        inputFile.close()
        outputFile.close()
        return True
    except:
        return False


def decodeHuffman(fileIn, fileOut):
    try:
        inputFile = open(fileIn, 'r')
        codes = {}
        lines = inputFile.readlines()
        inputFile.close()
        for line in range(0, len(lines) - 1):
            code = lines[line].split("+")
            codes[code[1].replace("\n", "")] = code[0]
        outputFile = open(fileOut, "w")
        encode = lines.pop()
        tmp = ""
        for char in encode:
            tmp += char
            if codes.get(tmp) is None:
                continue
            if codes[tmp] == "\\n":  # костыль для нормального декодирования переноса строки
                codes[tmp] = "\n"
            outputFile.write(codes[tmp])
            tmp = ""
        outputFile.close()
        return True
    except:
        return False


def encodeLZ(fileIn, fileOut):
    try:
        inputFile = open(fileIn, 'r')
        s = inputFile.read()
        code = ""
        dict = {}
        tmp = ""
        index = 1
        for i in range(0, len(s)):
            tmp += s[i]
            if (dict.get(tmp)) is None:
                if (dict.get(tmp[0:len(tmp) - 1])) is None:
                    code = code + "0," + tmp + "_"
                    dict[tmp] = index
                    index += 1
                    tmp = ""
                    continue
                else:
                    code = code + str(dict.get(tmp[0:len(tmp) - 1])) + "," + s[i] + "_"
                    dict[tmp] = index
                    index += 1
                    tmp = ""
                    continue
            if i == len(s) - 1:
                code = code + str(dict.get(tmp)) + "," + "-"
        outputFile = open(fileOut, "w")
        outputFile.write(code)
        outputFile.close()
        return True
    except:
        return False


def decodeLZ(fileIn, fileOut):
    try:
        inputFile = open(fileIn, 'r')
        s = inputFile.read().split("_")
        if "" in s:
            s.remove("")
        index = 1
        dict = {}
        decode = ""
        for item in s:
            i = item[0:item.find(",")]
            c = item[item.find(",") + 1:]
            if c == "-": c = ""
            if i == "0":
                decode = decode + c
                dict[str(index)] = c
                index += 1
                continue
            decode = decode + dict[str(i)] + c
            dict[str(index)] = dict[str(i)] + c
            index += 1
        outputFile = open(fileOut, "w")
        outputFile.write(decode)
        outputFile.close()
        return True
    except:
        return False


if (encodeHuffman("inc.txt", "huffman_encode.txt") and
        decodeHuffman("huffman_encode.txt", "huffman_decode.txt") and
        encodeLZ("inc.txt", "lz_encode.txt") and
        decodeLZ("lz_encode.txt", "lz_decode.txt")):
    print("Сжатие успешно!")
inc = open("inc.txt", "r")
huffman_encode = open("huffman_encode.txt", "r")
lz_encode = open("lz_encode.txt", "r")

incCount = len(inc.read());
huffmanCount = len(huffman_encode.read())
lzCount = len(lz_encode.read())

print("Исходное кол-во символов: ", incCount)
print("Кол-во символов после использования метода Хаффмана: ", huffmanCount)
print("Коэффициет сжатия: ", huffmanCount / incCount)
print("Кол-во символов после использования метода Лемпеля-Зива: ", lzCount)
print("Коэффициет сжатия: ", lzCount / incCount)

inc.close()
huffman_encode.close()
lz_encode.close()
