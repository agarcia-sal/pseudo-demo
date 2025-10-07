import math

class Solution:
    def minimumArrayLength(self, nums):
        helper_minima = nums[0]
        helper_counter = 1
        helper_index = 1
        while helper_index < len(nums):
            if nums[helper_index] < helper_minima:
                helper_minima = nums[helper_index]
                helper_counter = 1
            elif nums[helper_index] == helper_minima:
                helper_counter += 1
            helper_index += 1

        if helper_counter == 1:
            return 1

        temp_result = (helper_counter / 2) + 0.5
        return math.floor(temp_result)