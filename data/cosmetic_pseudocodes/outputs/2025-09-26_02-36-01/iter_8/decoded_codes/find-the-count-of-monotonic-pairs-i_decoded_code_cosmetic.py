class Solution:
    def countOfPairs(self, nums):
        TOL = 1000000007
        LIN = len(nums)
        step = 1  # (3 - 2) inferred as 1 from pseudocode context
        LMT = LIN - step
        CAP = 0

        for IDX in range(0, LMT, step):
            TMP1 = nums[IDX]
            if CAP < TMP1:
                CAP = TMP1

        cache = [None] * LIN
        pos = 0
        while pos < LIN:
            inner_arr = [None] * (CAP + step)
            pos2 = 0
            while pos2 < (CAP + step):
                inner_most_arr = [0] * (CAP + step)
                inner_arr[pos2] = inner_most_arr
                pos2 += step
            cache[pos] = inner_arr
            pos += step

        idxA = 0
        val0 = nums[0]
        while idxA <= val0:
            idxB = val0 - idxA
            cache[0][idxA][idxB] = 1
            idxA += step

        idx_outer = step
        while idx_outer < LIN:
            val_outer = nums[idx_outer]
            idx_mid = 0
            while idx_mid <= val_outer:
                idx_mid_cmpl = val_outer - idx_mid
                idx_inner1 = 0
                while idx_inner1 <= idx_mid:
                    idx_inner2 = idx_mid_cmpl
                    while idx_inner2 <= CAP:
                        hold_old = cache[idx_outer][idx_mid][idx_mid_cmpl]
                        hold_add = cache[idx_outer - step][idx_inner1][idx_inner2]
                        temp_sum = hold_old + hold_add
                        cache[idx_outer][idx_mid][idx_mid_cmpl] = temp_sum % TOL
                        idx_inner2 += step
                    idx_inner1 += step
                idx_mid += step
            idx_outer += step

        accumulator = 0
        ii = 0
        last_val = nums[LIN - step]
        while True:
            jj = 0
            while jj <= CAP:
                if ii + jj == last_val:
                    accumulator = (accumulator + cache[LIN - step][ii][jj]) % TOL
                jj += step
            ii += step
            if ii > CAP:
                break

        return accumulator