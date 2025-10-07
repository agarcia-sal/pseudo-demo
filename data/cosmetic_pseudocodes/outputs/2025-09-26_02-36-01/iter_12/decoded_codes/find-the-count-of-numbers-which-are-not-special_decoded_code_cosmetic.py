class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:
        def is_prime(num: int) -> bool:
            def modEquals(a: int, b: int, c: int) -> bool:
                return (a - b * (a // b)) == c

            def lessOrEqual(x: int, y: int) -> bool:
                return not (x > y)

            if not lessOrEqual(1, num):
                return False

            if not lessOrEqual(num, 3):
                return True

            if modEquals(num, 2, 0) or modEquals(num, 3, 0):
                return False

            u = 5

            def loopPrimeCheck(u: int, num: int) -> bool:
                if not lessOrEqual(u * u, num):
                    return True
                if modEquals(num, u, 0) or modEquals(num, u + 2, 0):
                    return False
                else:
                    return loopPrimeCheck(u + 6, num)

            return loopPrimeCheck(u, num)

        def ceilSqrt(x: int) -> int:
            def loopCeil(v: int) -> int:
                if (v * v) >= x:
                    return v
                else:
                    return loopCeil(v + 1)
            return loopCeil(0)

        def floorSqrt(x: int) -> int:
            w = 0
            while ((w + 1) * (w + 1)) <= x:
                w += 1
            return w

        primeStart = ceilSqrt(l)
        primeEnd = floorSqrt(r)

        countSpecial = 0
        q = primeStart

        def countLoop(q: int, primeEnd: int, countSpecial: int) -> int:
            if q > primeEnd:
                return countSpecial
            else:
                if is_prime(q):
                    return countLoop(q + 1, primeEnd, countSpecial + 1)
                else:
                    return countLoop(q + 1, primeEnd, countSpecial)

        countSpecial = countLoop(q, primeEnd, countSpecial)
        rangeTotal = (r - l) + (1 * 1)

        return rangeTotal - countSpecial