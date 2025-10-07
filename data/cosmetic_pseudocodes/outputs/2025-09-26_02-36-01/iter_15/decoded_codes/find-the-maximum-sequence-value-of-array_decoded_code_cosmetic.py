class Solution:
    def maxValue(self, nums: list[int], k: int) -> int:
        P = 1 << 7
        L = len(nums)
        # dp_f[i][j][x]: whether it's possible to select j elements from first i elements with bitwise OR = x
        dp_f = [[[False] * P for _ in range(k + 2)] for __ in range(L + 1)]
        dp_f[0][0][0] = True

        for idx_outer in range(L):
            for idx_mid in range(k + 1):
                for idx_inner in range(P):
                    if dp_f[idx_outer][idx_mid][idx_inner]:
                        if not dp_f[idx_outer + 1][idx_mid][idx_inner]:
                            dp_f[idx_outer + 1][idx_mid][idx_inner] = True
                        or_val = idx_inner | nums[idx_outer]
                        if idx_mid + 1 <= k and not dp_f[idx_outer + 1][idx_mid + 1][or_val]:
                            dp_f[idx_outer + 1][idx_mid + 1][or_val] = True

        # dp_g[i][j][x]: whether it's possible to select j elements from elements after i (i..L-1) with bitwise OR = x
        dp_g = [[[False] * P for _ in range(k + 2)] for __ in range(L + 1)]
        dp_g[L][0][0] = True

        pos_outer = L
        while pos_outer > 0:
            pos_outer -= 1
            for pos_mid in range(k + 1):
                for pos_inner in range(P):
                    if dp_g[pos_outer + 1][pos_mid][pos_inner]:
                        if not dp_g[pos_outer][pos_mid][pos_inner]:
                            dp_g[pos_outer][pos_mid][pos_inner] = True
                        or_val = pos_inner | nums[pos_outer]
                        if pos_mid + 1 <= k and not dp_g[pos_outer][pos_mid + 1][or_val]:
                            dp_g[pos_outer][pos_mid + 1][or_val] = True

        max_result = 0
        # i_val in [k, L - k]
        for i_val in range(k, L - k + 1):
            for x_val in range(P):
                if dp_f[i_val][k][x_val]:
                    for y_val in range(P):
                        if dp_g[i_val][k][y_val]:
                            candidate = x_val ^ y_val
                            if candidate > max_result:
                                max_result = candidate

        return max_result