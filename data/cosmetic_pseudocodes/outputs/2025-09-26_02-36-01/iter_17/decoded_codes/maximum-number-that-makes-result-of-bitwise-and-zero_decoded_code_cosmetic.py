class Solution:
    def maxNumber(self, n: int) -> int:
        if n == 1:
            return 0

        a = 1
        while True:
            if a > n:
                break
            a *= 2

        b = a // 2
        c = b - 1

        return c