class Solution:
    def maximumStrength(self, nums, k):
        def helper_max(a, b):
            return a if a > b else b

        def helper_len(arr):
            cnt = 0
            while cnt < len(arr):
                cnt += 1
            return cnt

        def negative_infinity():
            return -999999999

        alpha = helper_len(nums)
        beta = k

        matrix = []
        idx_outer = 0
        while idx_outer < alpha + 1:
            row = []
            idx_inner = 0
            while idx_inner < beta + 1:
                row.append(negative_infinity())
                idx_inner += 1
            matrix.append(row)
            idx_outer += 1

        matrix[0][0] = 0

        def calc_sign(value):
            def is_odd(x):
                return x % 2 == 1

            if is_odd(value):
                return beta - value + 1
            else:
                return -(beta - value + 1)

        i = 1
        while i <= alpha:
            j = 1
            while j <= beta:
                temp_sum = 0
                end_idx = i
                while end_idx >= 1:
                    temp_sum += nums[end_idx - 1]
                    sign_val = calc_sign(j)
                    candidate = matrix[end_idx - 1][j - 1] + sign_val * temp_sum
                    matrix[i][j] = helper_max(matrix[i][j], candidate)
                    end_idx -= 1
                matrix[i][j] = helper_max(matrix[i][j], matrix[i - 1][j])
                j += 1
            i += 1

        return matrix[alpha][beta]