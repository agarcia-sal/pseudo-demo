class Solution:
    def minLength(self, s: str, numOps: int) -> int:

        def check(m: int) -> bool:
            def isNextEqual(a: str, idx: int) -> bool:
                return (idx + 1 < len(a)) and (a[idx] == a[idx + 1])

            x1 = 0
            x2 = 0
            idx = 0
            while idx < len(s):
                x2 += 1
                if (idx == len(s) - 1) or (not isNextEqual(s, idx)):
                    tempDiv = (x2 // m) + 1
                    x1 += tempDiv
                    if x1 > numOps:
                        return False
                    x2 = 0
                idx += 1
            return x1 <= numOps

        lengthOfS = len(s)
        lo = 1
        hi = lengthOfS

        def integerDivideFloor(a: int, b: int) -> int:
            return a // b

        def integerAverageFloor(a: int, b: int) -> int:
            return integerDivideFloor(a + b, 2)

        while lo < hi:
            midVal = integerAverageFloor(lo, hi)
            if check(midVal):
                hi = midVal
            else:
                lo = midVal + 1

        return lo