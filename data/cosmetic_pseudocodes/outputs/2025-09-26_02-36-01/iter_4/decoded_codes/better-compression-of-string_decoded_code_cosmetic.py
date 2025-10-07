from collections import defaultdict

class Solution:
    def betterCompression(self, compressed: str) -> str:
        charTotals = defaultdict(int)
        activeChar = ""
        tally = 0
        idx = 0

        while idx < len(compressed):
            symbol = compressed[idx]
            if ('a' <= symbol <= 'z') or ('A' <= symbol <= 'Z'):
                if activeChar != "":
                    charTotals[activeChar] += tally
                activeChar = symbol
                tally = 0
            else:
                numericValue = int(symbol)
                tally = tally * 10 + numericValue
            idx += 1

        if activeChar != "":
            charTotals[activeChar] += tally

        partsList = []
        sortedKeys = sorted(charTotals)

        i = 0
        while i < len(sortedKeys):
            keyChar = sortedKeys[i]
            countVal = charTotals[keyChar]
            combinedString = keyChar + str(countVal)
            partsList.append(combinedString)
            i += 1

        finalResult = ""
        j = 0
        while j < len(partsList):
            finalResult += partsList[j]
            j += 1

        return finalResult