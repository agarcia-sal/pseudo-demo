class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: list[int]) -> int:
        CONST_MOD = 1_000_000_001

        transition = [[0] * 26 for _ in range(26)]
        for idx_outer in range(26):
            upper_bound = nums[idx_outer]
            for idx_inner in range(upper_bound):
                target_pos = (idx_outer + idx_inner + 1) % 26
                transition[idx_outer][target_pos] = (transition[idx_outer][target_pos] + 1) % CONST_MOD

        def matrix_multiply(A: list[list[int]], B: list[list[int]]) -> list[list[int]]:
            R = [[0] * 26 for _ in range(26)]
            for row in range(26):
                for col in range(26):
                    acc = 0
                    for k in range(26):
                        acc += A[row][k] * B[k][col]
                    R[row][col] = acc % CONST_MOD
            return R

        def matrix_power(matrix: list[list[int]], power: int) -> list[list[int]]:
            I = [[1 if i == j else 0 for j in range(26)] for i in range(26)]
            base_matrix = matrix
            exponent = power
            while exponent > 0:
                if exponent % 2 == 1:
                    I = matrix_multiply(I, base_matrix)
                base_matrix = matrix_multiply(base_matrix, base_matrix)
                exponent //= 2
            return I

        powered_matrix = matrix_power(transition, t)

        count_vec = [0] * 26
        for char in s:
            char_ind = ord(char) - ord('a')
            count_vec[char_ind] += 1

        final_vector = [0] * 26
        for ind_i in range(26):
            for ind_j in range(26):
                prod_val = (count_vec[ind_i] * powered_matrix[ind_i][ind_j]) % CONST_MOD
                final_vector[ind_j] = (final_vector[ind_j] + prod_val) % CONST_MOD

        result_sum = 0
        for val in final_vector:
            result_sum = (result_sum + val) % CONST_MOD

        return result_sum