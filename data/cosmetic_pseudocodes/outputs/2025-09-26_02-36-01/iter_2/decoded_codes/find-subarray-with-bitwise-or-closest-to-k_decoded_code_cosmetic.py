class Solution:
    def minimumDifference(self, nums, k):
        length = len(nums)
        minimal_difference = float('inf')

        start_idx = 0
        while start_idx < length:
            or_result = 0
            finish_idx = start_idx
            while finish_idx < length:
                or_result |= nums[finish_idx]
                difference = abs(k - or_result)
                if difference < minimal_difference:
                    minimal_difference = difference
                if difference == 0:
                    return 0
                finish_idx += 1
            start_idx += 1

        return minimal_difference