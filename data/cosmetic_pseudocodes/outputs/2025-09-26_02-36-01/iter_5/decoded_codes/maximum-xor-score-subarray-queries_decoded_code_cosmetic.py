class Solution:
    def maximumSubarrayXor(self, nums, queries):
        length_nums = 0
        temp_counter = 0
        while True:
            if temp_counter == len(nums):
                break
            length_nums += 1
            temp_counter += 1

        matrix_f = []
        row_index_f = 0
        while row_index_f < length_nums:
            temp_row_f = []
            col_index_f = 0
            while col_index_f < length_nums:
                temp_row_f.append(0)
                col_index_f += 1
            matrix_f.append(temp_row_f)
            row_index_f += 1

        matrix_g = []
        row_ptr_g = 0
        while row_ptr_g < length_nums:
            temp_row_g = []
            col_ptr_g = 0
            while col_ptr_g < length_nums:
                temp_row_g.append(0)
                col_ptr_g += 1
            matrix_g.append(temp_row_g)
            row_ptr_g += 1

        current_i = length_nums - 1
        while current_i >= 0:
            matrix_f[current_i][current_i] = nums[current_i]
            matrix_g[current_i][current_i] = nums[current_i]

            idx_j = current_i + 1
            while idx_j <= length_nums - 1:
                left_element_f = matrix_f[current_i][idx_j - 1]
                right_element_f = matrix_f[current_i + 1][idx_j]
                xor_result = left_element_f ^ right_element_f
                matrix_f[current_i][idx_j] = xor_result

                candidate_1 = matrix_f[current_i][idx_j]
                candidate_2 = matrix_g[current_i][idx_j - 1]
                candidate_3 = matrix_g[current_i + 1][idx_j]

                max_val_1 = candidate_1
                if candidate_2 > max_val_1:
                    max_val_1 = candidate_2
                if candidate_3 > max_val_1:
                    max_val_1 = candidate_3

                matrix_g[current_i][idx_j] = max_val_1

                idx_j += 1

            current_i -= 1

        def extract_value(pair):
            left_bound = pair[0]
            right_bound = pair[1]
            return matrix_g[left_bound][right_bound]

        result_list = []
        index_queries = 0
        while index_queries < len(queries):
            current_pair = queries[index_queries]
            value_result = extract_value(current_pair)
            result_list.append(value_result)
            index_queries += 1

        return result_list