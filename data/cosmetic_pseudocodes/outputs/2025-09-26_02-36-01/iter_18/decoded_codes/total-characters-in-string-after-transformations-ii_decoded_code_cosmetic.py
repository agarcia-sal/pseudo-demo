class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: list[int]) -> int:
        CONST_MOD = 1_000_000_001

        matrix_transformation = [[0] * 26 for _ in range(26)]

        for index_i in range(26):
            index_j = 0
            while True:
                if index_j >= nums[index_i]:
                    break
                column_index = (index_i + index_j + 1) % 26
                matrix_transformation[index_i][column_index] += 1
                index_j += 1

        def multiply_matrices(M1: list[list[int]], M2: list[list[int]]) -> list[list[int]]:
            mat_res = [[0] * 26 for _ in range(26)]
            for idx_i in range(26):
                for idx_j in range(26):
                    val = 0
                    for idx_k in range(26):
                        val += (M1[idx_i][idx_k] * M2[idx_k][idx_j]) % CONST_MOD
                    mat_res[idx_i][idx_j] = val % CONST_MOD
            return mat_res

        def power_matrix(base_mat: list[list[int]], exponent: int) -> list[list[int]]:
            identity_mat = [[1 if i == j else 0 for j in range(26)] for i in range(26)]
            current_base = base_mat
            exp_counter = exponent
            while exp_counter != 0:
                if exp_counter & 1:
                    identity_mat = multiply_matrices(identity_mat, current_base)
                current_base = multiply_matrices(current_base, current_base)
                exp_counter >>= 1
            return identity_mat

        powered_matrix = power_matrix(matrix_transformation, t)

        count_chars = [0] * 26
        for ch in s:
            pos_val = ord(ch) - ord('a')
            count_chars[pos_val] += 1

        final_counting = [0] * 26
        for idx_i in range(26):
            for idx_j in range(26):
                addition_val = (count_chars[idx_i] * powered_matrix[idx_i][idx_j]) % CONST_MOD
                final_counting[idx_j] = (final_counting[idx_j] + addition_val) % CONST_MOD

        acc_sum = 0
        for element in final_counting:
            acc_sum = (acc_sum + element) % CONST_MOD

        return acc_sum