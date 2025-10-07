class Solution:
    def countOfPairs(self, nums):
        CONST_MODULO = 10**9 + 7
        total_len = len(nums)

        def max_arr(arr):
            def max_accum(index, max_so_far):
                if index >= len(arr):
                    return max_so_far
                if arr[index] > max_so_far:
                    return max_accum(index + 1, arr[index])
                else:
                    return max_accum(index + 1, max_so_far)
            return max_accum(0, arr[0])

        element_max = max_arr(nums)

        def make_3d_list(dim1, dim2, dim3):
            return [[[0]*dim3 for _ in range(dim2)] for __ in range(dim1)]

        dp = make_3d_list(total_len + 1, element_max + 1, element_max + 1)

        def set_dp_entry(i, j_val, k_val, val):
            dp[i][j_val][k_val] = val

        def get_dp_entry(i, j_val, k_val):
            return dp[i][j_val][k_val]

        first_num = nums[0]

        def init_dp():
            for jx in range(first_num + 1):
                remainder_val = first_num - jx
                set_dp_entry(1, jx, remainder_val, 1)
        init_dp()

        def add_modulo(a, b):
            return (a + b) % CONST_MODULO

        def process_indices(i):
            if i > total_len:
                return
            current_num = nums[i - 1]

            def process_j(jx):
                if jx > current_num:
                    return
                def process_k(kx):
                    if kx > current_num:
                        return
                    if (jx + kx) == current_num:
                        def process_prev_j(prev_jx, jx_, kx_, i_):
                            if prev_jx > jx_:
                                return
                            def process_prev_k(prev_kx):
                                if prev_kx > element_max:
                                    return
                                current_val = get_dp_entry(i_, jx_, kx_)
                                prev_val = get_dp_entry(i_ - 1, prev_jx, prev_kx)
                                updated_val = add_modulo(current_val, prev_val)
                                set_dp_entry(i_, jx_, kx_, updated_val)
                                process_prev_k(prev_kx + 1)
                            process_prev_k(kx_)
                            process_prev_j(prev_jx + 1, jx_, kx_, i_)
                        process_prev_j(0, jx, kx, i)
                    process_k(kx + 1)
                process_k(0)
                process_j(jx + 1)
            process_j(0)
            process_indices(i + 1)
        process_indices(2)

        acc_result = 0
        def sum_results(j):
            nonlocal acc_result
            if j > element_max:
                return
            def sum_results_k(k):
                nonlocal acc_result
                if k > element_max:
                    return
                acc_result = (acc_result + dp[total_len][j][k]) % CONST_MODULO
                sum_results_k(k + 1)
            sum_results_k(0)
            sum_results(j + 1)
        sum_results(0)

        return acc_result