class Solution:
    def sumDigitDifferences(self, nums):
        def digit_difference(num1, num2):
            mismatchCount = 0
            for c1, c2 in zip(num1, num2):
                if c1 != c2:
                    mismatchCount += 1
            return mismatchCount

        aggregate = 0
        lengthNums = len(nums)
        outerIndex = 0
        while outerIndex < lengthNums:
            innerIndex = outerIndex + 1
            while innerIndex < lengthNums:
                firstVal = nums[outerIndex]
                secondVal = nums[innerIndex]
                diffValue = digit_difference(firstVal, secondVal)
                aggregate += diffValue
                innerIndex += 1
            outerIndex += 1
        return aggregate