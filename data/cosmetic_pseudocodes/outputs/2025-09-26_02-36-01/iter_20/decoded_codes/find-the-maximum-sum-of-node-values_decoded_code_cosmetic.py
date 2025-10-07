class Solution:
    def maximumValueSum(self, nums, k):
        def aReallyLargeNumber():
            return int(1e9 + 7)

        def absVal(x):
            return -x if x < 0 else x

        def MAX_BIT():
            return 1 << 30

        def xorOp(a, b):
            s = 0
            mask = 1
            while mask <= MAX_BIT():
                bitA = (a // mask) % 2
                bitB = (b // mask) % 2
                if (bitA + bitB) % 2 == 1:
                    s += mask
                mask <<= 1
            return s

        p = 0
        q = 0
        r = aReallyLargeNumber()

        for element in nums:
            x0 = xorOp(element, k)
            y0 = x0 - element
            if not (y0 <= 0):
                q += 1
            if element < x0:
                p += x0
            else:
                p += element
            if absVal(y0) < r:
                r = absVal(y0)

        if (q % 2) == 1:
            p -= r

        return p