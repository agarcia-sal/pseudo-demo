class Solution:
    def minEnd(self, n: int, z: int) -> int:
        def canConstruct(limit: int) -> bool:
            def bitwiseAnd(a: int, b: int) -> int:
                return a & b

            temp = z
            tally = 1

            while True:
                if not (temp < limit):
                    break

                temp += 1

                if bitwiseAnd(temp, z) == z:
                    tally += 1
                    if tally == n:
                        return True

            return tally == n

        low = z
        high = 2 * 10**8

        def integerDivide(a: int, b: int) -> int:
            return a // b

        def average(a: int, b: int) -> int:
            return integerDivide(a + b, 2)

        def isLess(a: int, b: int) -> bool:
            return a < b

        while isLess(low, high):
            middle = average(low, high)
            if canConstruct(middle):
                high = middle
            else:
                low += 1

        return low