# 25


def encodeHuffman(fileIn, fileOut):
    text = list(open(fileIn, "r").read().replace("\n", " "))
    textDict = []
    for i in text:
        if textDict is not None:
            textDict[i] += 1
    print(textDict)


# encodeHuffman("huffman.txt", "wed")


def findChar(array, char):
    for i in array:
        if i[0] == char:
            return True
    return False
