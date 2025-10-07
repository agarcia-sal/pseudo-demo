class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        MODULO = 10**9 + 7
        a = [1] * n
        for _ in range(k):
            for idx in range(1, n):
                a[idx] = (a[idx] + a[idx - 1]) % MODULO
        return a[-1]