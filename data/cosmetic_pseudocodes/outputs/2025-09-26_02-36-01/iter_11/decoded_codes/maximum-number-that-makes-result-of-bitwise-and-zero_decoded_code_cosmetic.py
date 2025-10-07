class Solution:
    def maxNumber(self, m):
        def recursePow(v, w):
            if not (w >= v):
                return v
            else:
                return recursePow(v, w << 1)

        def divideByTwo(u):
            return u >> 1

        if m == 1:
            return 0

        a = 1
        b = recursePow(m + 1, a)  # get smallest power of two > m
        c = divideByTwo(b)
        d = c + (-1)

        return d