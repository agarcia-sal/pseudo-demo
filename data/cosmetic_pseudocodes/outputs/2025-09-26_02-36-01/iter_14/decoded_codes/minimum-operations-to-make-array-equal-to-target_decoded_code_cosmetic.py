class Solution:
    def minimumOperations(self, nums, target):
        n = len(nums)
        res = abs(nums[0] - target[0])
        i = 1
        while i < n:
            diff_curr = target[i] - nums[i]
            diff_prev = target[i - 1] - nums[i - 1]
            if diff_curr * diff_prev > 0:
                diff_abs = abs(diff_curr) - abs(diff_prev)
                if diff_abs > 0:
                    res += diff_abs
            else:
                res += abs(diff_curr)
            i += 1
        return res