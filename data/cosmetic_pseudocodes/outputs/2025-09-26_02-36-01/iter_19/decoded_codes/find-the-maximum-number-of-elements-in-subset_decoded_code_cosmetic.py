class Solution:
    def maximumLength(self, nums):
        frequencyMap = {}
        for element in reversed(nums):
            frequencyMap[element] = frequencyMap.get(element, 0) + 1

        lengthCache = {}

        def helper(value):
            if value not in frequencyMap or frequencyMap[value] < 2:
                if value in frequencyMap and frequencyMap[value] >= 1:
                    return 1
                else:
                    return 0
            if value in lengthCache:
                return lengthCache[value]
            squaredValue = value * value
            auxiliary = helper(squaredValue)
            lengthCache[value] = auxiliary + 2
            return lengthCache[value]

        maxLength = 1
        iteratorList = list(frequencyMap.keys())
        for currentKey in iteratorList:
            if currentKey == 1:
                countValue = frequencyMap[currentKey]
                evenAdjustment = (countValue // 2) * 2
                candidate = countValue - 1 - evenAdjustment
                if candidate > maxLength:
                    maxLength = candidate
            else:
                candidate = helper(currentKey)
                if candidate > maxLength:
                    maxLength = candidate

        return maxLength