class Solution:
    def sumDigitDifferences(self, nums):
        def digit_difference(a, b):
            diffCount = 0
            pos = 0  # zero-based indexing in Python
            length = len(a)
            while pos < length:
                if a[pos] != b[pos]:
                    diffCount += 1
                pos += 1
            return diffCount

        result = 0
        lengthNums = len(nums)

        idxOuter = 0
        while idxOuter < lengthNums - 1:
            idxInner = idxOuter + 1
            while idxInner < lengthNums:
                result += digit_difference(nums[idxOuter], nums[idxInner])
                idxInner += 1
            idxOuter += 1

        return result