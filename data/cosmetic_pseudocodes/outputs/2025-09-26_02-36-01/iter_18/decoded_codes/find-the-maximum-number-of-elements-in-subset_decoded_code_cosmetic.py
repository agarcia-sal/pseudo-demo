from collections import Counter

class Solution:
    def maximumLength(self, nums):
        freqMap = Counter(nums)
        memo = {}

        def recurse(y):
            if y not in freqMap or freqMap[y] < 2:
                return 1 if y in freqMap and freqMap[y] >= 1 else 0
            if y in memo:
                return memo[y]
            squared = y * y
            tempVal = recurse(squared) + 2
            memo[y] = tempVal
            return tempVal

        bestLen = 1
        keysList = list(freqMap.keys())
        indexVar = 0

        while indexVar < len(keysList):
            currentKey = keysList[indexVar]
            if currentKey == 1:
                occ = freqMap[currentKey]
                adjusted = occ - 1 - ((occ % 2) * 2)
                if adjusted > bestLen:
                    bestLen = adjusted
            else:
                candidate = recurse(currentKey)
                if candidate > bestLen:
                    bestLen = candidate
            indexVar += 1

        return bestLen