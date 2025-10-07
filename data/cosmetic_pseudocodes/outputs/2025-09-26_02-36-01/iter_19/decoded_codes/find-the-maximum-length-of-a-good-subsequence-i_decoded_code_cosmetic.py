class Solution:
    def maximumLength(self, nums: list[int], k: int) -> int:
        alpha = len(nums)
        beta = [[1] * (k + 1) for _ in range(alpha)]
        omega = 0
        idx_outer = 0
        while idx_outer < alpha:
            val_outer = nums[idx_outer]
            idx_mid = 0
            while idx_mid <= k:
                idx_inner = 0
                while idx_inner < idx_outer:
                    val_inner = nums[idx_inner]
                    if val_outer == val_inner:
                        delta = beta[idx_inner][idx_mid] + 1
                        if beta[idx_outer][idx_mid] < delta:
                            beta[idx_outer][idx_mid] = delta
                    else:
                        if idx_mid > 0:
                            temp_val = beta[idx_inner][idx_mid - 1] + 1
                            if beta[idx_outer][idx_mid] < temp_val:
                                beta[idx_outer][idx_mid] = temp_val
                    idx_inner += 1
                idx_mid += 1
            if omega < beta[idx_outer][k]:
                omega = beta[idx_outer][k]
            idx_outer += 1
        return omega