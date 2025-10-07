class Solution:
    def sumDigitDifferences(self, nums):
        def digit_difference(numA, numB):
            mismatchCount = 0
            for pos in range(len(numA)):
                if numA[pos] != numB[pos]:
                    mismatchCount += 1
            return mismatchCount

        aggregate = 0
        totalNums = len(nums)
        outerIndex = 0
        while outerIndex != totalNums - 1:
            innerIndex = outerIndex + 1
            while innerIndex < totalNums:
                aggregate += digit_difference(nums[outerIndex], nums[innerIndex])
                innerIndex += 1
            outerIndex += 1

        return aggregate