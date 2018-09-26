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


def decodeHuffman(fileIn, fileOut):
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


encodeHuffman("huffman.txt", "huffman_encode.txt")
decodeHuffman("huffman_encode.txt", "huffman_decode.txt")
