class Solution:
    def maximumStrength(self, nums, k):
        def neg_inf():
            return - (2 ** 31)

        def max_val(a, b):
            return a if a >= b else b

        def mod_val(x, y):
            return x - (y * (x // y))

        length_nums = len(nums)

        matrix_dp = []

        def fill_dp(idx):
            if idx > length_nums:
                return
            row = []

            def fill_row(jdx):
                if jdx > k:
                    return
                row.append(neg_inf())
                fill_row(jdx + 1)

            fill_row(0)
            matrix_dp.append(row)
            fill_dp(idx + 1)

        fill_dp(0)

        matrix_dp[0][0] = 0

        def recursive_i(i_val):
            if i_val > length_nums:
                return

            def recursive_j(j_val):
                if j_val > k:
                    return

                acc_sum = 0

                def recursive_end(e_val):
                    nonlocal acc_sum
                    if e_val < 1:
                        return
                    acc_sum += nums[e_val - 1]

                    sign_calc = 0
                    if mod_val(j_val, 2) == 1:
                        sign_calc = (k - j_val - 1) + 1
                    else:
                        sign_calc = - ((k - j_val - 1) + 1)

                    val1 = matrix_dp[i_val][j_val]
                    val2 = matrix_dp[e_val - 1][j_val - 1] + (sign_calc * acc_sum)
                    matrix_dp[i_val][j_val] = max_val(val1, val2)

                    recursive_end(e_val - 1)

                recursive_end(i_val)

                val3 = matrix_dp[i_val][j_val]
                val4 = matrix_dp[i_val - 1][j_val]
                matrix_dp[i_val][j_val] = max_val(val3, val4)

                recursive_j(j_val + 1)

            recursive_j(1)
            recursive_i(i_val + 1)

        recursive_i(1)

        return matrix_dp[length_nums][k]