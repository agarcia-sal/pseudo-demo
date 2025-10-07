class Solution:
    def betterCompression(self, compressed: str) -> str:
        def isAlpha(ch: str) -> bool:
            return ("A" <= ch <= "Z") or ("a" <= ch <= "z")

        def strToInt(strVal: str) -> int:
            acc = 0
            idx = 0
            length = len(strVal)
            while idx < length:
                acc = acc * 10 + (ord(strVal[idx]) - ord("0"))
                idx += 1
            return acc

        def sortedKeys(dictObj: dict) -> list:
            keyList = list(dictObj.keys())
            n = len(keyList)
            while n > 1:
                newN = 0
                for i in range(1, n):
                    if keyList[i - 1] > keyList[i]:
                        keyList[i - 1], keyList[i] = keyList[i], keyList[i - 1]
                        newN = i
                n = newN
            return keyList

        def dictGetOrZero(dictionary: dict, key: str) -> int:
            return dictionary.get(key, 0)

        charAccum = {}
        curLetter = ""
        curNumStr = ""

        def processNumber():
            nonlocal curLetter, curNumStr
            if curLetter != "":
                currentTotal = dictGetOrZero(charAccum, curLetter)
                parsedCount = strToInt(curNumStr)
                charAccum[curLetter] = currentTotal + parsedCount
            curNumStr = ""

        def betterCompressionHelper(idx: int):
            nonlocal curLetter, curNumStr
            if idx > len(compressed):
                processNumber()
                return
            ch = compressed[idx - 1]
            if isAlpha(ch):
                processNumber()
                curLetter = ch
            else:
                curNumStr += ch
            betterCompressionHelper(idx + 1)

        curLetter = ""
        curNumStr = ""
        betterCompressionHelper(1)

        resultParts = []

        def appendParts(sortedList: list, pos: int):
            if pos > len(sortedList):
                return
            cKey = sortedList[pos - 1]
            val = charAccum[cKey]
            part = cKey + str(val)
            resultParts.append(part)
            appendParts(sortedList, pos + 1)

        sortedChars = sortedKeys(charAccum)
        appendParts(sortedChars, 1)

        outputString = "".join(resultParts)
        return outputString