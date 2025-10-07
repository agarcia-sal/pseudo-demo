from math import inf

class Solution:
    def minimumDifference(self, nums, k):
        length_of_nums = len(nums)
        minimal_difference = inf

        outer_idx = 0
        while outer_idx <= length_of_nums - 1:
            or_value = 0
            inner_idx = outer_idx
            while inner_idx <= length_of_nums - 1:
                or_value |= nums[inner_idx]
                difference = abs(k - or_value)
                if difference < minimal_difference:
                    minimal_difference = difference
                if difference == 0:
                    return 0
                inner_idx += 1
            outer_idx += 1

        return minimal_difference