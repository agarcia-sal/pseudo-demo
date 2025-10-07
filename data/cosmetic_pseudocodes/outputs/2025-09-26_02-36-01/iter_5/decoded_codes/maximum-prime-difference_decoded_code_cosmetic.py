class Solution:
    def maximumPrimeDifference(self, nums):
        prime_values = {
            2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37,
            41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83,
            89, 97
        }

        def helper_find_indices(current_pos, current_first, current_last):
            if current_pos >= len(nums):
                return -1 if current_first == -1 else current_last - current_first
            current_element = nums[current_pos]
            if current_element in prime_values:
                updated_first = current_pos if current_first == -1 else current_first
                updated_last = current_pos
            else:
                updated_first = current_first
                updated_last = current_last
            return helper_find_indices(current_pos + 1, updated_first, updated_last)

        return helper_find_indices(0, -1, -1)