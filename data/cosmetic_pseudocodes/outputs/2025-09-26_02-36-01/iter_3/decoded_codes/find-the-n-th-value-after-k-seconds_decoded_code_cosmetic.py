class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        MODULUS = 10**9 + 7
        sequence = [1] * n

        for _ in range(k):
            for idx in range(1, n):
                sum_val = sequence[idx] + sequence[idx - 1]
                sequence[idx] = sum_val % MODULUS

        return sequence[-1]