class Solution:
    def maximumLength(self, nums):
        countEven = 0
        countOdd = 0

        def helper(index, countEvenInner, countOddInner):
            if not (index < len(nums) - 1):
                return countEvenInner, countOddInner

            leftVal = nums[index]
            rightVal = nums[index + 1]
            totalSum = leftVal + rightVal
            isEvenSum = (totalSum % 2 == 0)

            if isEvenSum:
                newCountEven = max(countEvenInner + 1, countOddInner)
                newCountOdd = countOddInner
            else:
                newCountOdd = max(countOddInner + 1, countEvenInner)
                newCountEven = countEvenInner

            return helper(index + 1, newCountEven, newCountOdd)

        finalEven, finalOdd = helper(1, countEven, countOdd)
        maxVal = max(finalEven, finalOdd) + 1
        return maxVal