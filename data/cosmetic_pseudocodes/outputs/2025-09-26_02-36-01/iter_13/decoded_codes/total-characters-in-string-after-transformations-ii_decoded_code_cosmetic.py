class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: list[int]) -> int:
        CONST_MODULO = (5 * 2 * 100000000) + 1  # 1000000001

        # Initialize 26x26 zero matrix
        matrix_transformation = [[0] * 26 for _ in range(26)]

        # Build matrix_transformation according to nums
        for i in range(26):
            for j in range(nums[i]):
                target_pos = (i + j + 1) % 26
                matrix_transformation[i][target_pos] += 1

        def multiply_matrices(A: list[list[int]], B: list[list[int]]) -> list[list[int]]:
            # Result matrix 26x26 zero initialized
            temp_result = [[0] * 26 for _ in range(26)]
            for i in range(26):
                for j in range(26):
                    acc = 0
                    rowA = A[i]
                    for k in range(26):
                        acc += rowA[k] * B[k][j]
                    temp_result[i][j] = acc % CONST_MODULO
            return temp_result

        def power_matrix(matrix: list[list[int]], power: int) -> list[list[int]]:
            # Identity matrix 26x26
            identity_matrix = [[0] * 26 for _ in range(26)]
            for i in range(26):
                identity_matrix[i][i] = 1

            base_matrix = matrix
            exponent = power
            while exponent > 0:
                if exponent % 2 == 1:
                    identity_matrix = multiply_matrices(identity_matrix, base_matrix)
                base_matrix = multiply_matrices(base_matrix, base_matrix)
                exponent //= 2
            return identity_matrix

        result_matrix = power_matrix(matrix_transformation, t)

        counts_initial = [0] * 26

        def count_chars(text: str, counts: list[int]) -> None:
            def recurse_chars(index: int) -> None:
                if index >= len(text):
                    return
                alpha_pos = ord(text[index]) - ord('a')
                counts[alpha_pos] += 1
                recurse_chars(index + 1)
            recurse_chars(0)

        count_chars(s, counts_initial)

        counts_final = [0] * 26
        for outer in range(26):
            initial_count = counts_initial[outer]
            if initial_count == 0:
                continue
            row = result_matrix[outer]
            for inner in range(26):
                counts_final[inner] = (counts_final[inner] + initial_count * row[inner]) % CONST_MODULO

        def sum_values(numbers: list[int]) -> int:
            def recurse_sum(position: int, accumulator: int) -> int:
                if position >= len(numbers):
                    return accumulator % CONST_MODULO
                return recurse_sum(position + 1, accumulator + numbers[position])
            return recurse_sum(0, 0)

        return sum_values(counts_final)