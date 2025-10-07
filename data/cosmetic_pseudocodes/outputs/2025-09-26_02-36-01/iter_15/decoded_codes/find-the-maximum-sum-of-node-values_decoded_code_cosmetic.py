class Solution:
    def maximumValueSum(self, nums: list[int], k: int) -> int:
        MOD = int(1e9 + 7)
        count_positive_diff = 0
        total_sum = 0
        min_abs_diff = MOD

        def abs_val(x: int) -> int:
            return -x if x < 0 else x

        for num in nums:
            xor_val = num ^ k
            diff = xor_val - num
            if diff > 0:
                count_positive_diff += 1
            total_sum += num if num > xor_val else xor_val
            abs_diff = abs_val(diff)
            if abs_diff < min_abs_diff:
                min_abs_diff = abs_diff

        if count_positive_diff % 2 != 0:
            total_sum -= min_abs_diff

        return total_sum