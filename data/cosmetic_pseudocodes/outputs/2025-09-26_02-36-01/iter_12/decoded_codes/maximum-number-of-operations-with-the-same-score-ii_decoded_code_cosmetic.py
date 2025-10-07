class Solution:
    def maxOperations(self, nums):
        def explore(startIndex, endIndex, targetSum, cacheMap):
            def checkPairSum(a, b):
                return (a + b) == targetSum

            if startIndex >= endIndex:
                return 0

            keyTriple = (startIndex, endIndex, targetSum)
            if keyTriple in cacheMap:
                return cacheMap[keyTriple]

            highestCount = 0

            tempVal1 = nums[startIndex]
            tempVal2 = nums[startIndex + 1]
            tempVal3 = nums[endIndex]
            tempVal4 = nums[endIndex - 1]

            if checkPairSum(tempVal1, tempVal2):
                candidateCount = 1 + explore(startIndex + 2, endIndex, targetSum, cacheMap)
                if candidateCount > highestCount:
                    highestCount = candidateCount

            if checkPairSum(tempVal4, tempVal3):
                candidateCount = 1 + explore(startIndex, endIndex - 2, targetSum, cacheMap)
                if candidateCount > highestCount:
                    highestCount = candidateCount

            if checkPairSum(tempVal1, tempVal3):
                candidateCount = 1 + explore(startIndex + 1, endIndex - 1, targetSum, cacheMap)
                if candidateCount > highestCount:
                    highestCount = candidateCount

            cacheMap[keyTriple] = highestCount
            return highestCount

        def createTargetSum(valA, valB):
            return valA + valB

        lenNums = len(nums)
        firstPairSum = createTargetSum(nums[0], nums[1])
        secondPairSum = createTargetSum(nums[lenNums - 2], nums[lenNums - 1])
        thirdPairSum = createTargetSum(nums[0], nums[lenNums - 1])

        result1 = 1 + explore(2, lenNums - 1, firstPairSum, {})
        result2 = 1 + explore(0, lenNums - 3, secondPairSum, {})
        result3 = 1 + explore(1, lenNums - 2, thirdPairSum, {})

        return max(result1, result2, result3)