class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: list[int]) -> int:
        MOD = 10**9 + 1

        trans_matrix = [[0] * 26 for _ in range(26)]
        for i in range(26):
            for j in range(nums[i]):
                trans_matrix[i][(i + j + 1) % 26] += 1

        def matrix_multiply(A: list[list[int]], B: list[list[int]]) -> list[list[int]]:
            result = [[0] * 26 for _ in range(26)]
            for i in range(26):
                for j in range(26):
                    acc = 0
                    rowA = A[i]
                    for k in range(26):
                        acc += rowA[k] * B[k][j]
                    result[i][j] = acc % MOD
            return result

        def matrix_power(matrix: list[list[int]], power: int) -> list[list[int]]:
            result = [[1 if i == j else 0 for j in range(26)] for i in range(26)]
            base = matrix
            while power > 0:
                if power & 1:
                    result = matrix_multiply(result, base)
                base = matrix_multiply(base, base)
                power >>= 1
            return result

        final_matrix = matrix_power(trans_matrix, t)

        current_count = [0] * 26
        for char in s:
            current_count[ord(char) - ord('a')] += 1

        final_count = [0] * 26
        for i in range(26):
            ci = current_count[i]
            row = final_matrix[i]
            for j in range(26):
                final_count[j] = (final_count[j] + ci * row[j]) % MOD

        return sum(final_count) % MOD