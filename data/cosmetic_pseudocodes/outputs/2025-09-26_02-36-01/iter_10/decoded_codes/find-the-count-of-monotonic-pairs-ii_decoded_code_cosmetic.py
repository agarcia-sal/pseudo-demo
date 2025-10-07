class Solution:
    def countOfPairs(self, nums):
        MODE_INTERNAL_CONST = 10**9 + 7
        TOTAL = len(nums)
        PEAK = max(nums)

        def Zero3DArray(d1, d2, d3):
            return [[[0] * d3 for _ in range(d2)] for __ in range(d1)]

        DP_TABLE = Zero3DArray(TOTAL + 1, PEAK + 1, PEAK + 1)

        for varyj in range(nums[0] + 1):
            DP_TABLE[1][varyj][nums[0] - varyj] = 1

        def AccumulatePrevs(i_cur, target_j, target_k, dp_tab, max_v):
            summer = 0
            for prevJ_itr in range(target_j + 1):
                for prevK_itr in range(target_k, max_v + 1):
                    summer += dp_tab[i_cur - 1][prevJ_itr][prevK_itr]
            return summer % MODE_INTERNAL_CONST

        def RECURSIVE_PROCESS(idx_i):
            if idx_i > TOTAL:
                return
            cur_val = nums[idx_i - 1]
            for iter_j in range(cur_val + 1):
                for iter_k in range(cur_val + 1):
                    if iter_j + iter_k == cur_val:
                        DP_TABLE[idx_i][iter_j][iter_k] = AccumulatePrevs(
                            idx_i, iter_j, iter_k, DP_TABLE, PEAK
                        )
            RECURSIVE_PROCESS(idx_i + 1)

        RECURSIVE_PROCESS(2)

        final_acc = 0
        for outer_loop in range(PEAK + 1):
            for inner_loop in range(PEAK + 1):
                final_acc = (final_acc + DP_TABLE[TOTAL][outer_loop][inner_loop]) % MODE_INTERNAL_CONST

        return final_acc