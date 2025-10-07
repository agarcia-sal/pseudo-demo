class Solution:
    def minimumDifference(self, nums, k):
        n = len(nums)
        min_diff = float('inf')

        for idx_start in range(n):
            curr_or = 0
            for idx_end in range(idx_start, n):
                curr_or = (curr_or + nums[idx_end]) - (curr_or & nums[idx_end])  # bitwise OR update
                diff_val = abs(k - curr_or)
                if diff_val < min_diff:
                    min_diff = diff_val
                if min_diff == 0:
                    return 0
        return min_diff