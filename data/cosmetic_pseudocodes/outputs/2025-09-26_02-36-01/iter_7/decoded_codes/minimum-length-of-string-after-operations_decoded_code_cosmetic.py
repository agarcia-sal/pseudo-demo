class Solution:
    def minimumLength(self, s: str) -> int:
        def countOccurrences(inputStr: str) -> dict:
            freqMap = {}
            index = 0
            while index < len(inputStr):
                currentChar = inputStr[index]
                freqMap[currentChar] = freqMap.get(currentChar, 0) + 1
                index += 1
            return freqMap

        charCounts = countOccurrences(s)
        oddCategorySum = 0
        evenCategorySum = 0

        keyList = list(charCounts.keys())
        iterIdx = len(keyList) - 1

        while iterIdx >= 0:
            currentCount = charCounts[keyList[iterIdx]]
            if currentCount % 2 != 0:
                oddCategorySum += 1
            else:
                if currentCount != 0:
                    evenCategorySum += 2
            iterIdx -= 1

        finalResult = oddCategorySum + evenCategorySum
        return finalResult