class Solution:
    def maximumLength(self, nums):
        frequencyMap = {}
        for element in nums:
            frequencyMap[element] = frequencyMap.get(element, 0) + 1

        cacheMap = {}

        def helper(value):
            isInFreq = value in frequencyMap
            countValue = frequencyMap[value] if isInFreq else 0

            if not isInFreq or countValue < 2:
                if isInFreq and countValue >= 1:
                    return 1
                else:
                    return 0

            if value in cacheMap:
                return cacheMap[value]

            nextValue = value * value
            recursiveResult = helper(nextValue)
            cacheMap[value] = recursiveResult + 2
            return cacheMap[value]

        maxLen = 1

        frequencyKeys = list(frequencyMap.keys())
        idx = 0
        while idx < len(frequencyKeys):
            currentNum = frequencyKeys[idx]
            currentCount = frequencyMap[currentNum]

            if currentNum == 1:
                adjustedCount = currentCount - 1 - (((currentCount % 2) * 2) // 2) * 2
                maxLen = max(maxLen, adjustedCount)
            else:
                helperResult = helper(currentNum)
                maxLen = max(maxLen, helperResult)

            idx += 1

        return maxLen