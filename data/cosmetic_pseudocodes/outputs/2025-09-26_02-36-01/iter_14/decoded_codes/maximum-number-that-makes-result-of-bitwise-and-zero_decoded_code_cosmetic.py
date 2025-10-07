class Solution:
    def maxNumber(self, n: int) -> int:
        result = 0
        if not (n != 1):
            result = 0
        else:
            alpha = 1
            while True:
                alpha += alpha
                if alpha > n:
                    break
            alpha //= 2
            result = alpha - 1
        return result