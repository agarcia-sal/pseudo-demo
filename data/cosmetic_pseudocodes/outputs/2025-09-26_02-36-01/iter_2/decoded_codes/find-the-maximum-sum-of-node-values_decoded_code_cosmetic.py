class Solution:
    def maximumValueSum(self, nums, k):
        accumulated_sum = 0
        positive_gain_counter = 0
        smallest_gain = float('inf')

        for element in nums:
            xor_result = element ^ k
            difference = xor_result - element
            if difference > 0:
                positive_gain_counter += 1
            if element > xor_result:
                accumulated_sum += element
            else:
                accumulated_sum += xor_result
            abs_difference = abs(difference)
            if smallest_gain > abs_difference:
                smallest_gain = abs_difference

        if positive_gain_counter % 2 != 0:
            accumulated_sum -= smallest_gain

        return accumulated_sum