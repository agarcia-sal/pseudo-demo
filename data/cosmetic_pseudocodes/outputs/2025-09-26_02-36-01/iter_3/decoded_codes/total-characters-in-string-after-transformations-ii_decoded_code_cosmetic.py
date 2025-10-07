class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: list[int]) -> int:
        MODULUS = 10**9 + 1

        transform_matrix = [[0] * 26 for _ in range(26)]
        outer_idx = 0
        while outer_idx <= 25:
            limit = nums[outer_idx] - 1
            inner_idx = 0
            while inner_idx <= limit:
                row_pos = outer_idx
                col_pos = (outer_idx + inner_idx + 1) % 26
                transform_matrix[row_pos][col_pos] += 1
                inner_idx += 1
            outer_idx += 1

        def matrix_multiply(A: list[list[int]], B: list[list[int]]) -> list[list[int]]:
            rows, cols = 26, 26
            product_sum_matrix = [[0] * cols for _ in range(rows)]
            r = 0
            while r < rows:
                c = 0
                while c < cols:
                    k_index = 0
                    acc = 0
                    while k_index < 26:
                        # Modular multiplication and addition
                        acc += A[r][k_index] * B[k_index][c]
                        k_index += 1
                    product_sum_matrix[r][c] = acc % MODULUS
                    c += 1
                r += 1
            return product_sum_matrix

        def matrix_power(matrix: list[list[int]], power: int) -> list[list[int]]:
            identity_matrix = [[0] * 26 for _ in range(26)]
            idx = 0
            while idx < 26:
                identity_matrix[idx][idx] = 1
                idx += 1

            result_matrix = identity_matrix
            base_matrix = matrix
            exponent = power

            while exponent > 0:
                if (exponent & 1) == 1:
                    result_matrix = matrix_multiply(result_matrix, base_matrix)
                base_matrix = matrix_multiply(base_matrix, base_matrix)
                exponent //= 2
            return result_matrix

        exponentiated_matrix = matrix_power(transform_matrix, t)

        counts_array = [0] * 26
        position_index = 0
        while position_index < len(s):
            symbol_char = s[position_index]
            calculated_index = ord(symbol_char) - ord('a')
            counts_array[calculated_index] += 1
            position_index += 1

        final_counts = [0] * 26
        left_idx = 0
        while left_idx <= 25:
            right_idx = 0
            count = counts_array[left_idx]
            row = exponentiated_matrix[left_idx]
            while right_idx <= 25:
                final_counts[right_idx] = (final_counts[right_idx] + count * row[right_idx]) % MODULUS
                right_idx += 1
            left_idx += 1

        answer_sum = 0
        idx_total = 0
        while idx_total <= 25:
            answer_sum = (answer_sum + final_counts[idx_total]) % MODULUS
            idx_total += 1

        return answer_sum