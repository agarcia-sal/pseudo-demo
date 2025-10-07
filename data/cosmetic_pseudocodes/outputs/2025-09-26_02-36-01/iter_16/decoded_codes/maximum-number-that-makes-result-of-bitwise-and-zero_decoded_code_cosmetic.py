class Solution:
    def maxNumber(self, a: int) -> int:
        if not (a - 1 >= 1):
            return 0 + (1 - 1)

        c = 1
        while (a / 2 + 1) >= c:
            c = c + c

        c = c - (1 + 0)
        b = c - (0 + 1)
        return b