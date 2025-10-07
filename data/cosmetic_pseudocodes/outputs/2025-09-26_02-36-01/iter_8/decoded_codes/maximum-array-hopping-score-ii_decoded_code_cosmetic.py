from typing import List

class Solution:
    def maxScore(self, nums: List[int]) -> int:
        length_value = len(nums)
        temp_list = [0] * length_value
        index_marker = length_value - 2
        while index_marker >= 0:
            maximal_value = 0
            inner_counter = index_marker + 1
            while inner_counter <= length_value - 2:
                current_score = (inner_counter - index_marker) * nums[inner_counter]
                potential_max = current_score + temp_list[inner_counter]
                if maximal_value < potential_max:
                    maximal_value = potential_max
                inner_counter += 1
            temp_list[index_marker] = maximal_value
            index_marker -= 1
        return temp_list[0]