class Solution:
    def minOrAfterOperations(self, nums, k):
        def canAchieve(target_or):
            acc_and = -1
            op_count = 0
            idx = 0
            n = len(nums)
            while idx < n:
                current_num = nums[idx]
                if acc_and == -1:
                    acc_and = current_num
                else:
                    acc_and &= current_num
                if (acc_and & target_or) == 0:
                    acc_and = -1
                else:
                    op_count += 1
                    if op_count > k:
                        return False
                idx += 1
            return True

        max_val = (1 << 30) - 1
        res = max_val
        bit_idx = 0
        while bit_idx < 30:
            mask = 1 << bit_idx
            if (res & mask) == 0:
                bit_idx += 1
                continue
            inv_res_mask = ~(res ^ mask)
            if canAchieve(inv_res_mask):
                res &= ~mask
            bit_idx += 1
        return res