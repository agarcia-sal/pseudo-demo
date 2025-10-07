class Solution:
    def maximumValueSum(self, nums, k):
        sum_total = 0
        count_positive_gain = 0
        smallest_gain = float('inf')

        for current_num in nums:
            value_xor = current_num ^ k
            difference = value_xor - current_num

            if difference > 0:
                count_positive_gain += 1

            max_val = max(current_num, value_xor)
            sum_total += max_val

            abs_diff = abs(difference)
            if abs_diff < smallest_gain:
                smallest_gain = abs_diff

        if count_positive_gain % 2 == 1:
            sum_total -= smallest_gain

        return sum_total