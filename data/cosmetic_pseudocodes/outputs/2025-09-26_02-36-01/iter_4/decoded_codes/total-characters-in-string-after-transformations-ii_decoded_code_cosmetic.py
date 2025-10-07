class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: list[int]) -> int:
        MODULUS = 10 ** 9 + 1
        SIZE = 26

        # Build transition grid
        transition_grid = [[0] * SIZE for _ in range(SIZE)]
        outer_index = 0
        while outer_index < SIZE:
            inner_limit = nums[outer_index]
            inner_index = 0
            while inner_index < inner_limit:
                target_pos = (outer_index + inner_index + 1) % SIZE
                transition_grid[outer_index][target_pos] += 1
                inner_index += 1
            outer_index += 1

        def matrix_multiply(A: list[list[int]], B: list[list[int]]) -> list[list[int]]:
            product_matrix = [[0] * SIZE for _ in range(SIZE)]
            row_index = 0
            while row_index < SIZE:
                col_index = 0
                while col_index < SIZE:
                    sum_accumulator = 0
                    k_index = 0
                    while k_index < SIZE:
                        partial_mul = A[row_index][k_index] * B[k_index][col_index]
                        sum_accumulator += partial_mul
                        k_index += 1
                    product_matrix[row_index][col_index] = sum_accumulator % MODULUS
                    col_index += 1
                row_index += 1
            return product_matrix

        def matrix_power(matrix: list[list[int]], power: int) -> list[list[int]]:
            identity_matrix = [[1 if x == y else 0 for y in range(SIZE)] for x in range(SIZE)]
            exponent_base = matrix
            exponent_counter = power

            while exponent_counter > 0:
                if exponent_counter % 2 != 0:
                    identity_matrix = matrix_multiply(identity_matrix, exponent_base)
                exponent_base = matrix_multiply(exponent_base, exponent_base)
                exponent_counter //= 2

            return identity_matrix

        powered_matrix = matrix_power(transition_grid, t)

        letter_freq = [0] * SIZE
        for ch in s:
            char_pos = ord(ch) - ord('a')
            letter_freq[char_pos] += 1

        transformed_freq = [0] * SIZE
        idx_outer = 0
        while idx_outer < SIZE:
            idx_inner = 0
            while idx_inner < SIZE:
                addition_val = letter_freq[idx_outer] * powered_matrix[idx_outer][idx_inner]
                transformed_freq[idx_inner] = (transformed_freq[idx_inner] + addition_val) % MODULUS
                idx_inner += 1
            idx_outer += 1

        total_sum = 0
        sum_index = 0
        while sum_index < SIZE:
            total_sum = (total_sum + transformed_freq[sum_index]) % MODULUS
            sum_index += 1

        return total_sum