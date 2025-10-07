from collections import defaultdict

class Solution:
    def betterCompression(self, compressed: str) -> str:
        def isLetter(ch: str) -> bool:
            return ('A' <= ch <= 'Z') or ('a' <= ch <= 'z')

        def accumulateCounts(index: int, currentSymbol: str, currentTotal: int, countsDict: dict):
            if index == len(compressed):
                if currentSymbol != '':
                    countsDict[currentSymbol] += currentTotal
                return

            charAtIndex = compressed[index]
            if isLetter(charAtIndex):
                if currentSymbol != '':
                    countsDict[currentSymbol] += currentTotal
                accumulateCounts(index + 1, charAtIndex, 0, countsDict)
            else:
                updatedTotal = currentTotal * 10 + (ord(charAtIndex) - ord('0'))
                accumulateCounts(index + 1, currentSymbol, updatedTotal, countsDict)

        counts = defaultdict(int)
        accumulateCounts(0, "", 0, counts)

        keysList = list(counts.keys())

        def compareAlpha(a: str, b: str) -> bool:
            return a > b

        sortedKeys = []
        while len(keysList) != 0:
            maxIndex = 0
            i = 1
            while i < len(keysList):
                if compareAlpha(sortedKeys[maxIndex] if maxIndex < len(sortedKeys) else keysList[0], keysList[i]):
                    maxIndex = i
                i += 1
            sortedKeys.append(keysList[maxIndex])
            keysList.pop(maxIndex)
        sortedKeys.reverse()

        parts = []
        idx = 0
        while idx < len(sortedKeys):
            sym = sortedKeys[idx]
            val = counts[sym]
            if val == 0:
                valStr = '0'
            else:
                digits = []
                tmpVal = val
                while tmpVal != 0:
                    digits.append(str(tmpVal % 10))
                    tmpVal //= 10
                digits.reverse()
                valStr = ''.join(digits)
            parts.append(sym + valStr)
            idx += 1

        outputStr = ''.join(parts)
        return outputStr