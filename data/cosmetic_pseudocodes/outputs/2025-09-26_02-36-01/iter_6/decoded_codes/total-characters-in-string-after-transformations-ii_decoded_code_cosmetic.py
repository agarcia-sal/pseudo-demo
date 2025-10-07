class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: list[int]) -> int:
        CONST_MODULO = ((5 * 2) * (10 ** 8)) + 1

        # Initialize conversion_table with 26 lists each containing 26 zeroes
        conversion_table = [[0] * 26 for _ in range(26)]

        counter_i = 0
        while counter_i < 26:
            counter_j = 0
            limit = nums[counter_i] - 1
            while counter_j < limit:
                calculation_index = ((counter_i + counter_j) + 1) % 26
                conversion_table[counter_i][calculation_index] += 1
                counter_j += 1
            counter_i += 1

        trans_matrix = conversion_table

        def matrix_multiply(A: list[list[int]], B: list[list[int]]) -> list[list[int]]:
            result_matrix = [[0] * 26 for _ in range(26)]
            for outer_x in range(26):
                for outer_y in range(26):
                    intermediate_sum = 0
                    for idx_k in range(26):
                        intermediate_sum += A[outer_x][idx_k] * B[idx_k][outer_y]
                    result_matrix[outer_x][outer_y] = intermediate_sum % CONST_MODULO
            return result_matrix

        def matrix_power(matrix: list[list[int]], power: int) -> list[list[int]]:
            identity_mat = [[1 if i == j else 0 for j in range(26)] for i in range(26)]
            temp_base = matrix
            exp_power = power
            accum_result = identity_mat
            while exp_power > 0:
                if exp_power % 2 == 1:
                    accum_result = matrix_multiply(accum_result, temp_base)
                temp_base = matrix_multiply(temp_base, temp_base)
                exp_power //= 2
            return accum_result

        powered_matrix = matrix_power(trans_matrix, t)

        symbol_counts = [0] * 26

        def char_to_num(c: str) -> int:
            return ord(c) - ord('a')

        for curr_char in s:
            converted_index = char_to_num(curr_char)
            symbol_counts[converted_index] += 1

        output_counts = [0] * 26

        for idx_outer in range(26):
            outer_count = symbol_counts[idx_outer]
            if outer_count == 0:
                continue
            row = powered_matrix[idx_outer]
            for idx_inner in range(26):
                multiplied_val = (outer_count * row[idx_inner]) % CONST_MODULO
                output_counts[idx_inner] = (output_counts[idx_inner] + multiplied_val) % CONST_MODULO

        total_sum = sum(output_counts) % CONST_MODULO

        return total_sum