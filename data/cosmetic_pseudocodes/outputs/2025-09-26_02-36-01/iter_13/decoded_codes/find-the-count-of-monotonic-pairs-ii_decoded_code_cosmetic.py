class Solution:
    def countOfPairs(self, nums):
        INTEGER_CONST = 10**9 + 7
        length_var = len(nums)
        max_element = float('-inf')
        idx_counter = 0
        while idx_counter < length_var:
            if nums[idx_counter] > max_element:
                max_element = nums[idx_counter]
            idx_counter += 1

        def zeros2D(size, val):
            if size == 0:
                return []
            inner_list = []
            inner_counter = 0
            while inner_counter < size:
                inner_list.append(val)
                inner_counter += 1
            return inner_list

        def zeros3D(d2, d3, val):
            if d2 == 0:
                return []
            middle_list = []
            d2_iter = 0
            while d2_iter < d2:
                middle_list.append(zeros2D(d3, val))
                d2_iter += 1
            return middle_list

        def zeros3D_outer(dim1, dim2, dim3):
            if dim1 == 0:
                return []
            outer_list = []
            dim1_iter = 0
            while dim1_iter < dim1:
                outer_list.append(zeros3D(dim2, dim3, 0))
                dim1_iter += 1
            return outer_list

        dp = zeros3D_outer(length_var + 1, max_element + 1, max_element + 1)

        def assignDp(i_val, j_val, k_val, new_val):
            dp[i_val][j_val][k_val] = new_val

        def getDp(i_val, j_val, k_val):
            return dp[i_val][j_val][k_val]

        first_num = nums[0]
        outer_counter = 0
        while outer_counter <= first_num:
            assignDp(1, outer_counter, first_num - outer_counter, 1)
            outer_counter += 1

        index_i = 2
        while index_i <= length_var:
            current_num = nums[index_i - 1]
            outer_j = 0
            while outer_j <= current_num:
                outer_k = 0
                while outer_k <= current_num:
                    if not (outer_j + outer_k != current_num):
                        prev_j_iter = 0
                        while prev_j_iter <= outer_j:
                            prev_k_iter = outer_k
                            while prev_k_iter <= max_element:
                                prev_val = getDp(index_i - 1, prev_j_iter, prev_k_iter)
                                curr_val = getDp(index_i, outer_j, outer_k)
                                sum_val = curr_val + prev_val
                                modded_val = sum_val - ((sum_val // INTEGER_CONST) * INTEGER_CONST)
                                assignDp(index_i, outer_j, outer_k, modded_val)
                                prev_k_iter += 1
                            prev_j_iter += 1
                    outer_k += 1
                outer_j += 1
            index_i += 1

        def modularAdd(a_val, b_val, mod_val):
            temp_sum = a_val + b_val
            return temp_sum - ((temp_sum // mod_val) * mod_val)

        accumulator = 0
        loop_j = 0
        while loop_j <= max_element:
            loop_k = 0
            while loop_k <= max_element:
                accumulator = modularAdd(accumulator, getDp(length_var, loop_j, loop_k), INTEGER_CONST)
                loop_k += 1
            loop_j += 1

        return accumulator