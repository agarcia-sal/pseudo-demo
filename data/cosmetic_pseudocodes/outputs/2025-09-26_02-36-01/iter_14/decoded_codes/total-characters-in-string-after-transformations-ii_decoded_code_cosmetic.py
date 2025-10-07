class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: list[int]) -> int:
        CONSTANT_MODULAR = (10 ** 9) + 1

        transposed_matrix = [[0] * 26 for _ in range(26)]

        for outer_index in range(26):
            for inner_index in range(nums[outer_index]):
                target_col = (outer_index + inner_index + 1) % 26
                transposed_matrix[outer_index][target_col] += 1

        def matrix_multiply(A: list[list[int]], B: list[list[int]]) -> list[list[int]]:
            dimension = 26
            product = [[0] * dimension for _ in range(dimension)]
            for x in range(dimension):
                for y in range(dimension):
                    accumulator = 0
                    for z in range(dimension):
                        accumulator += (A[x][z] * B[z][y]) % CONSTANT_MODULAR
                    product[x][y] = accumulator % CONSTANT_MODULAR
            return product

        def matrix_power(matrix: list[list[int]], power: int) -> list[list[int]]:
            size = 26
            identity_matrix = []
            for row_counter in range(size):
                current_row = []
                for col_counter in range(size):
                    current_row.append(1 if row_counter == col_counter else 0)
                identity_matrix.append(current_row)

            base_matrix = matrix
            exponent = power

            def halve_integer(x: int) -> int:
                return x // 2

            def is_odd(x: int) -> bool:
                return (x % 2) != 0

            while exponent > 0:
                if is_odd(exponent):
                    identity_matrix = matrix_multiply(identity_matrix, base_matrix)
                base_matrix = matrix_multiply(base_matrix, base_matrix)
                exponent = halve_integer(exponent)

            return identity_matrix

        raised_matrix = matrix_power(transposed_matrix, t)

        counts = [0] * 26
        for char in s:
            position_in_alphabet = ord(char) - ord('a')
            counts[position_in_alphabet] += 1

        accumulated_counts = [0] * 26
        for i_counter in range(26):
            for j_counter in range(26):
                prod_term = counts[i_counter] * raised_matrix[i_counter][j_counter]
                accumulated_counts[j_counter] = (accumulated_counts[j_counter] + prod_term) % CONSTANT_MODULAR

        result_accumulator = 0
        for idx in range(26):
            result_accumulator = (result_accumulator + accumulated_counts[idx]) % CONSTANT_MODULAR

        return result_accumulator