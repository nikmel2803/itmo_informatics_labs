import math
from textwrap import wrap


class HammingEncoder:
    def __init__(self, dataBits):
        self.dataBits = dataBits
        degree = 0
        index = int(math.pow(2, degree) - 1)
        while index < dataBits:
            dataBits += 1
            degree += 1
            index = int(math.pow(2, degree) - 1)
        self.controlBits = degree

    def calculateControlBits(self, s):
        for d in range(self.controlBits):
            amount = 0
            length = int(math.pow(2, d))
            i = length - 1
            while i < len(s):
                amount += sum(int(i) for i in s[i:i + length])
                i = i + length * 2
            amount -= int(s[length - 1])
            if amount % 2 == 0:
                s[length - 1] = "0"
            else:
                s[length - 1] = "1"
        return s

    def encode(self, string):
        s1 = wrap(string, self.dataBits)
        result = ""
        for s in s1:
            s = list(s)
            degree = 0
            index = int(math.pow(2, degree) - 1)
            while index < len(s):
                s.insert(index, "0")
                degree += 1
                index = int(math.pow(2, degree) - 1)
            result += ''.join(self.calculateControlBits(s))
        return result

    def decode(self, string):
        s1 = wrap(string, self.dataBits + self.controlBits)
        i = 0
        for s in s1:
            s = list(s)

            originalS = self.calculateControlBits(s.copy())
            summa = 0
            for d in range(self.controlBits):
                ind = int(math.pow(2, d) - 1)
                if originalS[ind] != s[ind]:
                    summa += int(math.pow(2, d))
            if summa != 0:
                if s[summa - 1] == "0":
                    s[summa - 1] = "1"
                else:
                    s[summa - 1] = "0"
            s1[i] = ''.join(s)
            i += 1
        return "".join(s1)


hamm = HammingEncoder(8)
print("Hamming encode: ", hamm.encode("01000100"))
print("Hamming decode: ", hamm.decode("110111010100"))
