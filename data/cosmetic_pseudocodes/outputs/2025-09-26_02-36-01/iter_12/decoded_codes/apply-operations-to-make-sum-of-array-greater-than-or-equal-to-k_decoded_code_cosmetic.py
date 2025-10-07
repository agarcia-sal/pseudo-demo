class Solution:
    def minOperations(self, k: int) -> int:
        def intSqrt(n: int) -> int:
            r = 0
            c = 1
            while c * c <= n:
                r = c
                c += 1
            return r

        def intDivFloor(a: int, b: int) -> int:
            return (a - (a % b)) // b

        result = 9223372036854775807
        idx = 1
        limit = intSqrt(k) + 1

        while idx < limit:
            numerator = k + idx - 1
            denom = idx
            valY = intDivFloor(numerator, denom)
            sumOps = (idx - 1) + (valY - 1)

            if sumOps < result:
                result = sumOps

            idx += 1

        return result