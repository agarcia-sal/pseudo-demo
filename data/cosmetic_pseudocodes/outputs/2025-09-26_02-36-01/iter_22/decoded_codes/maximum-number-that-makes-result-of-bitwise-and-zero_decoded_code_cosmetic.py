class Solution:
    def maxNumber(self, n: int) -> int:
        p = 1
        if n == 1:
            return 0
        while p <= n:
            p = 1 + p + (p - 1)
        q = p // 2
        r = q - 1
        return r