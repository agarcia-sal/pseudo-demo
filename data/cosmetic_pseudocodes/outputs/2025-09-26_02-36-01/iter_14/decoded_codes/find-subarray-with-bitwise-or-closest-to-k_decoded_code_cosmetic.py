from math import inf

class Solution:
    def minimumDifference(self, nums, k):
        length_val = len(nums)
        minimum_gap = inf

        outer = 0
        while outer <= length_val - 1:
            accumulator = 0
            inner = outer
            while inner <= length_val - 1:
                accumulator |= nums[inner]
                difference = abs(k - accumulator)
                if difference < minimum_gap:
                    minimum_gap = difference
                if difference == 0:
                    return 0
                inner += 1
            outer += 1

        return minimum_gap