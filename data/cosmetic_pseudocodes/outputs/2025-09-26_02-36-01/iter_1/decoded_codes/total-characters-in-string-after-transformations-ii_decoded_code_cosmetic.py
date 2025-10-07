class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: list[int]) -> int:
        MOD = 10**9 + 1

        transformation_matrix = [[0] * 26 for _ in range(26)]
        for letter_idx in range(26):
            for step in range(nums[letter_idx]):
                target_idx = (letter_idx + step + 1) % 26
                transformation_matrix[letter_idx][target_idx] += 1

        def multiply_matrices(X: list[list[int]], Y: list[list[int]]) -> list[list[int]]:
            product = [[0] * 26 for _ in range(26)]
            for row in range(26):
                x_row = X[row]
                for col in range(26):
                    cell_sum = 0
                    for mid in range(26):
                        cell_sum += x_row[mid] * Y[mid][col]
                    product[row][col] = cell_sum % MOD
            return product

        def power_matrix(mat: list[list[int]], exp: int) -> list[list[int]]:
            identity = [[0] * 26 for _ in range(26)]
            for i in range(26):
                identity[i][i] = 1
            base_matrix = mat
            exponent = exp
            result_matrix = identity
            while exponent > 0:
                if exponent % 2 == 1:
                    result_matrix = multiply_matrices(result_matrix, base_matrix)
                base_matrix = multiply_matrices(base_matrix, base_matrix)
                exponent //= 2
            return result_matrix

        powered_matrix = power_matrix(transformation_matrix, t)

        frequency_vector = [0] * 26
        for character in s:
            frequency_vector[ord(character) - ord('a')] += 1

        final_vector = [0] * 26
        for from_idx in range(26):
            freq = frequency_vector[from_idx]
            powered_row = powered_matrix[from_idx]
            for to_idx in range(26):
                final_vector[to_idx] = (final_vector[to_idx] + freq * powered_row[to_idx]) % MOD

        return sum(final_vector) % MOD