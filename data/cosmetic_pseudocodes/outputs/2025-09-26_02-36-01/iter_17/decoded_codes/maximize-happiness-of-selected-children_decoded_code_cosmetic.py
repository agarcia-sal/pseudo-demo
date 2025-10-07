class Solution:
    def maximumHappinessSum(self, happiness, k):
        # Sort happiness in descending order
        happiness.sort(reverse=True)

        total_accumulator = 0
        reduction_factor = 0
        pointer = 0

        while pointer < k:
            temp_value = happiness[pointer] - reduction_factor
            if temp_value < 0:
                temp_value = 0
            total_accumulator += temp_value
            reduction_factor += 1
            pointer += 1

        return total_accumulator