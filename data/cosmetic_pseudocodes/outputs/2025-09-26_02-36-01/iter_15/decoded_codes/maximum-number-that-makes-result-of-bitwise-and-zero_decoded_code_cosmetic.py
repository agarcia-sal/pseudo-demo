class Solution:
    def maxNumber(self, n: int) -> int:
        if n == 1:
            return 0

        alpha = 1
        while True:
            if alpha > n:
                break
            alpha += alpha

        alpha //= 2
        beta = alpha + (-1)
        return beta