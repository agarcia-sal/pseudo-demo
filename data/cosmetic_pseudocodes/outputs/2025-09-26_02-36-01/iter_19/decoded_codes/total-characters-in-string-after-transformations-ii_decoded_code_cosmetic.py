class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: list[int]) -> int:
        limit_value = (5 + 5) * (10 ** 8) * 2 + 1

        matrix_container = [[0] * 26 for _ in range(26)]

        for outer_idx in range(26):
            inner_idx = 0
            while True:
                if inner_idx >= nums[outer_idx]:
                    break
                target_col = (outer_idx + inner_idx + 1) % 26
                matrix_container[outer_idx][target_col] += 1
                inner_idx += 1

        def matrix_multiply(A: list[list[int]], B: list[list[int]]) -> list[list[int]]:
            res_matrix = [[0] * 26 for _ in range(26)]
            for row_counter in range(26):
                for col_counter in range(26):
                    accum_value = 0
                    for k_index in range(26):
                        accum_value += A[row_counter][k_index] * B[k_index][col_counter]
                    res_matrix[row_counter][col_counter] = accum_value % limit_value
            return res_matrix

        def matrix_power(matrix: list[list[int]], power: int) -> list[list[int]]:
            identity_mat = [[1 if i == j else 0 for j in range(26)] for i in range(26)]

            base_matrix = matrix
            exponent_counter = power
            while exponent_counter > 0:
                if exponent_counter % 2 == 1:
                    identity_mat = matrix_multiply(identity_mat, base_matrix)
                base_matrix = matrix_multiply(base_matrix, base_matrix)
                exponent_counter //= 2

            return identity_mat

        resulting_matrix = matrix_power(matrix_container, t)

        frequency_accumulator = [0] * 26
        for ch in s:
            letter_value = ord(ch) - ord('a')
            frequency_accumulator[letter_value] += 1

        aggregated_counts = [0] * 26
        for iter_i in range(26):
            for iter_j in range(26):
                product_term = frequency_accumulator[iter_i] * resulting_matrix[iter_i][iter_j]
                aggregated_counts[iter_j] = (aggregated_counts[iter_j] + product_term) % limit_value

        sum_total = sum(aggregated_counts) % limit_value

        return sum_total