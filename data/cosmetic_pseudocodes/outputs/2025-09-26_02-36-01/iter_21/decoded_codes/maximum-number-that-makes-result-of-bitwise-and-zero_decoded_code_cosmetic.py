class Solution:
    def maxNumber(self, p: int) -> int:
        q = 0
        r = 1
        if not (p != 1):
            q = 0
        else:
            while True:
                if r > p:
                    break
                r = r + r
            r = r // 2
            q = r + (-1)
        return q