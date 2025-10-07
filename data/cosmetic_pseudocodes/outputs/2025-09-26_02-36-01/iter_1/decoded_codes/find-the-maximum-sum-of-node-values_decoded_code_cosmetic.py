class Solution:
    def maximumValueSum(self, nums, k):
        sum_total = 0
        count_positive_gain = 0
        smallest_gain = float('inf')

        for current_num in nums:
            xor_result = current_num ^ k
            difference = xor_result - current_num

            if difference > 0:
                count_positive_gain += 1

            sum_total += max(current_num, xor_result)
            smallest_gain = min(smallest_gain, abs(difference))

        if count_positive_gain % 2 != 0:
            sum_total -= smallest_gain

        return sum_total