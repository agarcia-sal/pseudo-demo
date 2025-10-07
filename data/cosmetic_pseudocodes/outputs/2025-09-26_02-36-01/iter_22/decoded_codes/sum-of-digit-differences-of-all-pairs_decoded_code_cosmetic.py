class Solution:
    def sumDigitDifferences(self, nums):
        def digit_difference(num1, num2):
            result = 0
            pos = 0
            while pos < len(num1):
                if num1[pos] != num2[pos]:
                    result += 1
                pos += 1
            return result

        aggregate = 0
        lengthVal = len(nums)
        leftIndex = 0
        while leftIndex < lengthVal:
            rightIndex = leftIndex + 1
            while rightIndex < lengthVal:
                aggregate += digit_difference(nums[leftIndex], nums[rightIndex])
                rightIndex += 1
            leftIndex += 1

        return aggregate