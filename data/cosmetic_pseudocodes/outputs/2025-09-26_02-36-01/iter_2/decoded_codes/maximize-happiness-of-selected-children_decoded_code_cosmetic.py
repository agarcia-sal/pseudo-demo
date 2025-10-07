class Solution:
    def maximumHappinessSum(self, happiness, k):
        sorted_list = sorted(happiness, reverse=True)
        total_happiness = 0
        reduction_counter = 0
        position = 0
        while position < k:
            adjusted_value = sorted_list[position] - reduction_counter
            if adjusted_value < 0:
                adjusted_value = 0
            total_happiness += adjusted_value
            reduction_counter += 1
            position += 1
        return total_happiness