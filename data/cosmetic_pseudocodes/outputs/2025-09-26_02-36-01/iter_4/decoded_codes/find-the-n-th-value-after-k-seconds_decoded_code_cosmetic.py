class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        MODULO_VALUE = 10**9 + 7
        numbers = [1] * n

        for _ in range(k):
            for i in range(1, n):
                numbers[i] = (numbers[i] + numbers[i - 1]) % MODULO_VALUE

        return numbers[-1]