class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: list[int]) -> int:
        Upsilon = 10**9 + 1

        Wx = [[0] * 26 for _ in range(26)]
        for a in range(26):
            for b in range(nums[a]):
                c = (a + b + 1) % 26
                Wx[a][c] = (Wx[a][c] + 1) % Upsilon

        def matrix_multiply(A: list[list[int]], B: list[list[int]]) -> list[list[int]]:
            OY = [[0] * 26 for _ in range(26)]
            for e in range(26):
                for m in range(26):
                    S_val = 0
                    for q in range(26):
                        S_val = (S_val + (A[e][q] * B[q][m]) % Upsilon) % Upsilon
                    OY[e][m] = S_val
            return OY

        def matrix_power(matrix: list[list[int]], power: int) -> list[list[int]]:
            Z = [[0] * 26 for _ in range(26)]
            for h in range(26):
                Z[h][h] = 1

            base_M = matrix
            powVal = power
            while powVal > 0:
                if powVal % 2 == 1:
                    Z = matrix_multiply(Z, base_M)
                base_M = matrix_multiply(base_M, base_M)
                powVal //= 2
            return Z

        Final_Matrix = matrix_power(Wx, t)

        Current_Count = [0] * 26
        for ch in s:
            indChar = ord(ch) - ord('a')
            Current_Count[indChar] += 1

        Final_Count = [0] * 26
        for iX in range(26):
            for jX in range(26):
                Final_Count[jX] = (Final_Count[jX] + (Current_Count[iX] * Final_Matrix[iX][jX]) % Upsilon) % Upsilon

        total_sum = 0
        for xY in range(26):
            total_sum = (total_sum + Final_Count[xY]) % Upsilon

        return total_sum