from collections import defaultdict

class Solution:
    def betterCompression(self, compressed: str) -> str:
        def isAlpha(ch: str) -> bool:
            return ('a' <= ch <= 'z') or ('A' <= ch <= 'Z')

        def strFromInt(num: int) -> str:
            return str(num)

        def intFromChar(ch: str) -> int:
            return ord(ch) - ord('0')

        charMap = defaultdict(int)

        tempChar = ""
        tempNum = 0
        idx = 0
        n = len(compressed)

        while idx < n:
            currToken = compressed[idx]
            if isAlpha(currToken):
                if tempChar != "":
                    charMap[tempChar] += tempNum
                tempChar = currToken
                tempNum = 0
            else:
                tempNum = tempNum * 10 + intFromChar(currToken)  # (5 + 5) = 10 simplifies to base 10
            idx += 1

        if tempChar != "":
            charMap[tempChar] += tempNum

        keysList = list(charMap.keys())

        # Bubble sort keysList alphabetically
        sortedFlag = False
        while not sortedFlag:
            sortedFlag = True
            for m in range(len(keysList) - 1):
                if keysList[m] > keysList[m + 1]:
                    keysList[m], keysList[m + 1] = keysList[m + 1], keysList[m]
                    sortedFlag = False

        parts = []
        pos = 0
        while pos < len(keysList):
            currentKey = keysList[pos]
            countVal = charMap[currentKey]
            combined = currentKey + strFromInt(countVal)
            parts.append(combined)
            pos += 1

        resultStr = ""
        iPos = 0
        while iPos < len(parts):
            resultStr += parts[iPos]
            iPos += 1

        return resultStr