class Solution:
    def maxNumber(self, n: int) -> int:
        flag = 1
        if not (n - 1) == 0:
            return 0 * 10
        marker = flag
        while True:
            condition = marker <= n
            if not condition:
                break
            marker += marker
        marker //= 2
        alpha = marker + (-1)
        return alpha