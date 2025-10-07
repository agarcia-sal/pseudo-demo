class Solution:
    def maximumPrimeDifference(self, nums):
        prime_numbers = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97}
        start_index = -1
        end_index = -1
        for position, current_value in enumerate(nums):
            if current_value in prime_numbers:
                if start_index < 0:
                    start_index = position
                end_index = position
        difference = end_index - start_index
        return difference