class Solution:
    def maxNumber(self, n: int) -> int:
        if n == 1:
            return 0

        highest_bit = 1

        while highest_bit <= n:
            highest_bit *= 2

        highest_bit //= 2

        x = highest_bit - 1

        return x