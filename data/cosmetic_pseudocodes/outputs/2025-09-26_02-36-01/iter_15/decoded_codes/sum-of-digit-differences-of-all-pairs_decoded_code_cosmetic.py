class Solution:
    def sumDigitDifferences(self, nums):
        def digit_difference(num1, num2):
            c = 0
            p = 0
            while p < len(num1):
                if num1[p] != num2[p]:
                    c += 1
                p += 1
            return c

        total = 0
        length_of_nums = len(nums)

        x = 0
        while x < length_of_nums:
            y = x + 1
            while y < length_of_nums:
                total += digit_difference(nums[x], nums[y])
                y += 1
            x += 1

        return total