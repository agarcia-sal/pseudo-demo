class Solution:
    def maxNumber(self, n: int) -> int:
        p = 1
        result = 0
        if n != 1:
            while True:
                if p <= n:
                    p += p
                else:
                    break
            p //= 2
            result = p - 1
        return result