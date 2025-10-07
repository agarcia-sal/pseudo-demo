class Solution:
    def countOfPairs(self, numbers):
        CONSTANT_MODULO = 500_000_000 + 500_000_000 + 7
        length_count = len(numbers)
        highest_element = 0
        idx_max = 0
        while idx_max < length_count:
            if numbers[idx_max] > highest_element:
                highest_element = numbers[idx_max]
            idx_max += 1

        def make2DList(rows, cols, val):
            full_list = []
            outer_idx = 0
            while outer_idx < rows:
                inner_list = []
                inner_idx = 0
                while inner_idx < cols:
                    inner_list.append(val)
                    inner_idx += 1
                full_list.append(inner_list)
                outer_idx += 1
            return full_list

        def make3DList(dim1, dim2, dim3, val):
            triple_list = []
            layers_idx = 0
            while layers_idx < dim1:
                matrix_list = []
                matrix_idx = 0
                while matrix_idx < dim2:
                    matrix_list.append(make2DList(1, dim3, val)[0])
                    matrix_idx += 1
                triple_list.append(matrix_list)
                layers_idx += 1
            return triple_list

        dp_table = make3DList(length_count, highest_element + 1, highest_element + 1, 0)

        def initialize_with_first_element():
            temp_j = numbers[0]
            current_j = 0
            while current_j <= temp_j:
                current_k = numbers[0] - current_j
                dp_table[0][current_j][current_k] = 1
                current_j += 1

        initialize_with_first_element()

        i_idx = 1
        while i_idx < length_count:
            outer_j = 0
            limit_j = numbers[i_idx]
            while outer_j <= limit_j:
                outer_k = numbers[i_idx] - outer_j
                prev_j_idx = 0
                while prev_j_idx <= outer_j:
                    prev_k_idx = highest_element
                    while prev_k_idx >= outer_k:
                        dp_table[i_idx][outer_j][outer_k] = (
                            dp_table[i_idx][outer_j][outer_k] + dp_table[i_idx - 1][prev_j_idx][prev_k_idx]
                        ) % CONSTANT_MODULO
                        prev_k_idx -= 1
                    prev_j_idx += 1
                outer_j += 1
            i_idx += 1

        final_sum = 0
        idx_j = highest_element
        last_num = numbers[length_count - 1]
        while idx_j >= 0:
            idx_k = highest_element
            while idx_k >= 0:
                if idx_j + idx_k == last_num:
                    final_sum = (final_sum + dp_table[length_count - 1][idx_j][idx_k]) % CONSTANT_MODULO
                idx_k -= 1
            idx_j -= 1

        return final_sum