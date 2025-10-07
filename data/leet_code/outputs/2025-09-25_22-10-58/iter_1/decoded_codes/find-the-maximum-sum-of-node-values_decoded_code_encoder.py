class Solution:
    def maximumValueSum(self, nums, k):
        total_sum = 0
        odd_gain_count = 0
        min_gain = float('inf')

        for num in nums:
            xor_value = num ^ k
            gain = xor_value - num
            if gain > 0:
                odd_gain_count += 1
            total_sum += max(num, xor_value)
            min_gain = min(min_gain, abs(gain))

        if odd_gain_count % 2 != 0:
            total_sum -= min_gain

        return total_sum