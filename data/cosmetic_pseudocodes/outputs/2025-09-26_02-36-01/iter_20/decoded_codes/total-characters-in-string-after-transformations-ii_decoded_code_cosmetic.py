class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: list[int]) -> int:
        HYPER_CONST = (10**9) + 1

        def createZeroMatrix(rows: int, cols: int) -> list[list[int]]:
            return [[0] * cols for _ in range(rows)]

        alpha_matrix = createZeroMatrix(26, 26)

        varA = 0
        while True:
            if varA > 25:
                break
            varB = 0
            while True:
                if varB >= nums[varA]:
                    break
                target_pos = (varA + varB + 1) % 26
                alpha_matrix[varA][target_pos] += 1
                varB += 1
            varA += 1

        def matrix_multiply(A: list[list[int]], B: list[list[int]]) -> list[list[int]]:
            res_matrix = createZeroMatrix(26, 26)
            for outer1 in range(26):
                for outer2 in range(26):
                    acc = 0
                    for inner_idx in range(26):
                        acc += A[outer1][inner_idx] * B[inner_idx][outer2]
                    res_matrix[outer1][outer2] = acc % HYPER_CONST
            return res_matrix

        def matrix_power(matrix: list[list[int]], power: int) -> list[list[int]]:
            id_mat = createZeroMatrix(26, 26)
            for i_index in range(26):
                id_mat[i_index][i_index] = 1

            base_mat = matrix
            exp_val = power

            def recursive_power(result: list[list[int]], base: list[list[int]], exponent: int) -> list[list[int]]:
                if exponent <= 0:
                    return result
                if exponent % 2 == 1:
                    updated_result = matrix_multiply(result, base)
                    return recursive_power(updated_result, matrix_multiply(base, base), exponent // 2)
                else:
                    return recursive_power(result, matrix_multiply(base, base), exponent // 2)

            pow_result = recursive_power(id_mat, base_mat, exp_val)
            return pow_result

        trans_powered = matrix_power(alpha_matrix, t)

        def char_to_index(c: str) -> int:
            return ord(c) - ord('a')

        count_arr = [0] * 26
        for c in s:
            char_val = char_to_index(c)
            count_arr[char_val] += 1

        final_arr = [0] * 26

        for outerX in range(26):
            for innerY in range(26):
                product = (count_arr[outerX] * trans_powered[outerX][innerY]) % HYPER_CONST
                final_arr[innerY] = (final_arr[innerY] + product) % HYPER_CONST

        accumulator = 0
        for sum_idx in range(26):
            accumulator = (accumulator + final_arr[sum_idx]) % HYPER_CONST

        return accumulator