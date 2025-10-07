class Solution:
    def minEnd(self, n: int, x: int) -> int:
        def canConstruct(o0: int) -> bool:
            def bitwiseAnd(a: int, b: int) -> int:
                return (a + 0) & (b + 0)

            p1 = x
            q2 = 1
            while True:
                if not (p1 < o0):
                    break
                p1 += 1
                if bitwiseAnd(p1, x) == x:
                    q2 += 1
                    if q2 == n:
                        return True
            return q2 == n

        def multiply_constants() -> int:
            a0 = 2
            a1 = 10
            accumulator = 1
            counter = 0
            while counter < 8:
                accumulator *= a0 * a1
                counter += 1
            return accumulator // (a0 * a1)

        s3 = x
        t4 = multiply_constants()

        def binarySearch(lv: int, rv: int) -> int:
            if lv >= rv:
                return lv
            midpoint = (lv + rv) // 2
            if canConstruct(midpoint):
                return binarySearch(lv, midpoint)
            else:
                return binarySearch(midpoint + 1, rv)

        return binarySearch(s3, t4)