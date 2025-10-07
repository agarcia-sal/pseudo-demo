class Solution:
    def sumDigitDifferences(self, nums):
        def digit_difference(a, b):
            mismatch_count = 0
            p = 0
            while p < len(a):
                if a[p] != b[p]:
                    mismatch_count += 1
                p += 1
            return mismatch_count

        accumulator = 0
        size = len(nums)
        x = 0
        while x < size - 1:
            y = x + 1
            while y < size:
                accumulator += digit_difference(nums[x], nums[y])
                y += 1
            x += 1
        return accumulator