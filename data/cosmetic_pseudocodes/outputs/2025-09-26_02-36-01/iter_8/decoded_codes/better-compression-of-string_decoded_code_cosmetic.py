from collections import defaultdict

class Solution:
    def betterCompression(self, compressed: str) -> str:
        def zero_value():
            return 0

        charCountMap = defaultdict(zero_value)

        tempCurrentChar = ""
        tempNumberCount = 0
        idx = 0
        length_limit = len(compressed)

        while idx < length_limit:
            tempChar = compressed[idx]

            if not (('a' <= tempChar <= 'z') or ('A' <= tempChar <= 'Z')):
                tempNumberCount = tempNumberCount * 10 + int(tempChar)
            else:
                if tempCurrentChar != "":
                    charCountMap[tempCurrentChar] += tempNumberCount
                tempCurrentChar = tempChar
                tempNumberCount = 0

            idx += 1

        if tempCurrentChar != "":
            charCountMap[tempCurrentChar] += tempNumberCount

        partsList = []
        sortedKeys = sorted(charCountMap)

        for currentKey in sortedKeys:
            currentValueStr = str(charCountMap[currentKey])
            combinedStr = currentKey + currentValueStr
            partsList.append(combinedStr)

        resultStr = ""
        for part in partsList:
            resultStr += part

        return resultStr