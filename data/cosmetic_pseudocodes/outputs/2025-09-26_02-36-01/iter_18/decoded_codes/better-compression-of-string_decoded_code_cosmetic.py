from collections import defaultdict

class Solution:
    def betterCompression(self, compressed: str) -> str:

        def accumulateCounts(sourceStr, idx, accDict, prevKey, prevVal):
            if idx >= len(sourceStr):
                if prevKey != "":
                    accDict[prevKey] += prevVal
                return accDict
            ch = sourceStr[idx]
            if ('A' <= ch <= 'Z') or ('a' <= ch <= 'z'):
                if prevKey != "":
                    accDict[prevKey] += prevVal
                return accumulateCounts(sourceStr, idx + 1, accDict, ch, 0)
            else:
                newVal = prevVal * 10 + (ord(ch) - 48)
                return accumulateCounts(sourceStr, idx + 1, accDict, prevKey, newVal)

        def builtInKeysSorted(dct):
            keyList = list(dct.keys())
            sortedList = []
            while keyList:
                minChar = keyList[0]
                for c in keyList:
                    if c < minChar:
                        minChar = c
                sortedList.append(minChar)
                keyList.remove(minChar)
            return sortedList

        def stringifyNumber(num):
            if num == 0:
                return "0"
            charsOut = []
            n = num
            while n > 0:
                rem = n - (n // 10) * 10
                digitChar = chr(rem + 48)
                charsOut.insert(0, digitChar)
                n = n // 10
            return "".join(charsOut)

        countsDictionary = defaultdict(int)
        accumulated = accumulateCounts(compressed, 0, countsDictionary, "", 0)

        partsList = []
        sortedKeys = builtInKeysSorted(accumulated)
        idxK = 0
        while idxK < len(sortedKeys):
            letter = sortedKeys[idxK]
            val = accumulated[letter]
            strVal = stringifyNumber(val)
            partsList.append(letter + strVal)
            idxK += 1

        outputString = ""
        for element in partsList:
            outputString += element

        return outputString