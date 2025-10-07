class Solution:
    def sumDigitDifferences(self, nums):
        def digit_difference(num1, num2):
            count = 0
            for d1, d2 in zip(str(num1), str(num2)):
                if d1 != d2:
                    count += 1
            return count

        total_sum = 0
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                total_sum += digit_difference(nums[i], nums[j])
        return total_sum