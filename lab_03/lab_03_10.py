# 24
text = open("text1.txt", "r").read().replace("\n", " ").split(" ")
textDict = dict.fromkeys(text, 0)
for i in text:
    if textDict.get(i) is not None:
        textDict[i] += 1
print(textDict)
