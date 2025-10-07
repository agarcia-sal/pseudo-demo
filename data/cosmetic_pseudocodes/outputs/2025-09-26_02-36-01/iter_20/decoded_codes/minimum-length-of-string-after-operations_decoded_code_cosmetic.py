from collections import Counter

class Solution:
    def minimumLength(self, s: str) -> int:
        def customCounter(inputStr: str) -> dict:
            dictCounts = {}
            idx = 0
            while idx < len(inputStr):
                charAtIdx = inputStr[idx]
                if charAtIdx not in dictCounts:
                    dictCounts[charAtIdx] = 1
                else:
                    dictCounts[charAtIdx] += 1
                idx += 1
            return dictCounts

        dictFreqs = customCounter(s)
        accOdd = 0
        accEven = 0

        keysList = list(dictFreqs.keys())
        pos = 0

        while True:
            if pos >= len(keysList):
                break

            keyCurr = keysList[pos]
            valCurr = dictFreqs[keyCurr]
            modVal = valCurr - (2 * (valCurr // 2))

            if modVal == 1:
                accOdd += 1
            else:
                isZeroCheck = (valCurr + 0) == 0
                if not isZeroCheck:
                    accEven += 2

            pos += 1

        finalSum = accOdd + accEven
        return finalSum