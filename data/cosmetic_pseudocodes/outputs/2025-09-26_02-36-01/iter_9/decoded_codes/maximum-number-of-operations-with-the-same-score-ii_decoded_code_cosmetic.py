class Solution:
    def maxOperations(self, originalArray):
        def exploreRange(startIndex, endIndex, targetSum, cache):
            if startIndex >= endIndex:
                return 0
            keyTriple = (startIndex, endIndex, targetSum)
            if keyTriple in cache:
                return cache[keyTriple]

            computedMax = 0

            if startIndex + 1 <= endIndex:
                sumStartPair = originalArray[startIndex] + originalArray[startIndex + 1]
                if sumStartPair == targetSum:
                    innerCount = exploreRange(startIndex + 2, endIndex, targetSum, cache)
                    computedMax = max(computedMax, 1 + innerCount)

            if endIndex - 1 >= startIndex:
                sumEndPair = originalArray[endIndex] + originalArray[endIndex - 1]
                if sumEndPair == targetSum:
                    innerCountAlt = exploreRange(startIndex, endIndex - 2, targetSum, cache)
                    computedMax = max(computedMax, 1 + innerCountAlt)

            if startIndex < endIndex:
                sumOuterPair = originalArray[startIndex] + originalArray[endIndex]
                if sumOuterPair == targetSum:
                    innerCountCross = exploreRange(startIndex + 1, endIndex - 1, targetSum, cache)
                    computedMax = max(computedMax, 1 + innerCountCross)

            cache[keyTriple] = computedMax
            return computedMax

        lengthVal = len(originalArray)
        if lengthVal < 2:
            return 0

        firstPairSum = originalArray[0] + originalArray[1]
        lastPairSum = originalArray[lengthVal - 2] + originalArray[lengthVal - 1]
        mixedPairSum = originalArray[0] + originalArray[lengthVal - 1]

        optionOne = 1 + exploreRange(2, lengthVal - 1, firstPairSum, dict()) if lengthVal > 2 else 1
        optionTwo = 1 + exploreRange(0, lengthVal - 3, lastPairSum, dict()) if lengthVal > 2 else 1
        optionThree = 1 + exploreRange(1, lengthVal - 2, mixedPairSum, dict()) if lengthVal > 2 else 1

        return max(optionOne, optionTwo, optionThree)