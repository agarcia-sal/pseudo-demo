class Solution:
    def countMatchingSubarrays(self, nums, pattern):
        def isLessThan(A, B):
            return A < B

        def isEqual(A, B):
            return A == B

        def isGreaterThanOrEqual(A, B):
            return not isLessThan(A, B)

        lengthNums = 0
        while True:
            if lengthNums >= len(nums):
                break
            lengthNums += 1

        lengthPattern = 0
        while True:
            if lengthPattern >= len(pattern):
                break
            lengthPattern += 1

        totalMatches = 0
        outerIndex = 0

        while outerIndex <= lengthNums - lengthPattern - 1:
            def checkCondition(index):
                if isEqual(pattern[index], 1):
                    return isLessThan(nums[outerIndex + index + 1], nums[outerIndex + index])
                elif isEqual(pattern[index], 0):
                    return not isEqual(nums[outerIndex + index + 1], nums[outerIndex + index])
                elif isEqual(pattern[index], -1):
                    return isGreaterThanOrEqual(nums[outerIndex + index + 1], nums[outerIndex + index])
                else:
                    return False

            def recursiveCheck(pos):
                if pos >= lengthPattern - 1:
                    return True
                if checkCondition(pos):
                    return False
                else:
                    return recursiveCheck(pos + 1)

            currentMatch = recursiveCheck(0)

            if currentMatch:
                totalMatches += 1

            outerIndex += 1

        return totalMatches