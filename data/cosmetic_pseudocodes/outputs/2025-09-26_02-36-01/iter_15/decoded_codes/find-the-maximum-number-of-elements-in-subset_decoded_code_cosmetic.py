from collections import Counter

class Solution:
    def maximumLength(self, nums):
        frequencyMap = Counter(nums)
        cache = {}

        def helper(y):
            if y not in frequencyMap or frequencyMap[y] < 2:
                if y in frequencyMap and frequencyMap[y] >= 1:
                    return 1
                else:
                    return 0
            if y in cache:
                return cache[y]
            accumulator = y * y
            cache[y] = helper(accumulator) + 2
            return cache[y]

        maximum = 1
        keysList = list(frequencyMap.keys())
        index = 0
        while index < len(keysList):
            currentKey = keysList[index]
            if currentKey == 1:
                freqVal = frequencyMap[currentKey]
                val1 = freqVal - 1
                val2 = (freqVal % 2) * 2
                candidate = val1 - val2
                if maximum < candidate:
                    maximum = candidate
            else:
                candidate2 = helper(currentKey)
                if maximum < candidate2:
                    maximum = candidate2
            index += 1

        return maximum