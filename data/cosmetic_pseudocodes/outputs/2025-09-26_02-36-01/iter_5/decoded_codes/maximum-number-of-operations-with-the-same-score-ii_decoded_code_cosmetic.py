class Solution:
    def maxOperations(self, nums):
        def explore(leftIndex, rightIndex, targetSum, cache):
            if not (leftIndex < rightIndex):
                return 0

            keyTuple = (leftIndex, rightIndex, targetSum)
            if keyTuple in cache:
                return cache[keyTuple]

            resultCount = 0

            if leftIndex + 1 <= rightIndex:
                firstPairSum = nums[leftIndex] + nums[leftIndex + 1]
                if firstPairSum == targetSum:
                    candidateResult = 1 + explore(leftIndex + 2, rightIndex, targetSum, cache)
                    if candidateResult > resultCount:
                        resultCount = candidateResult

            if rightIndex - 1 >= leftIndex:
                secondPairSum = nums[rightIndex] + nums[rightIndex - 1]
                if secondPairSum == targetSum:
                    candidateResult = 1 + explore(leftIndex, rightIndex - 2, targetSum, cache)
                    if candidateResult > resultCount:
                        resultCount = candidateResult

            crossPairSum = nums[leftIndex] + nums[rightIndex]
            if crossPairSum == targetSum:
                candidateResult = 1 + explore(leftIndex + 1, rightIndex - 1, targetSum, cache)
                if candidateResult > resultCount:
                    resultCount = candidateResult

            cache[keyTuple] = resultCount
            return resultCount

        lengthVal = len(nums)
        if lengthVal < 2:
            return 0

        firstTarget = nums[0] + nums[1]
        secondTarget = nums[lengthVal - 2] + nums[lengthVal - 1]
        thirdTarget = nums[0] + nums[lengthVal - 1]

        resultA = 1 + explore(2, lengthVal - 1, firstTarget, {}) if lengthVal > 2 else 1
        resultB = 1 + explore(0, lengthVal - 3, secondTarget, {}) if lengthVal > 3 else 1
        resultC = 1 + explore(1, lengthVal - 2, thirdTarget, {}) if lengthVal > 2 else 1

        finalResult = resultA
        if resultB > finalResult:
            finalResult = resultB
        if resultC > finalResult:
            finalResult = resultC

        return finalResult