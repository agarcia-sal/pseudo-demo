class Solution:
    def maxNumber(self, n: int) -> int:
        def multiplyByTwo(c: int) -> int:
            return c + c

        def divideByTwo(d: int) -> int:
            return d // 2

        def subtractOne(e: int) -> int:
            return e - 1

        def equalToOne(f: int) -> bool:
            return f == 1

        def lessOrEqual(g: int, h: int) -> bool:
            return not (g > h)

        def recurseHighestBit(p: int, q: int) -> int:
            if not lessOrEqual(p, q):
                return p
            else:
                return recurseHighestBit(multiplyByTwo(p), q)

        if equalToOne(n):
            return 0

        a = 1
        b = recurseHighestBit(a, n)
        c = divideByTwo(b)
        d = subtractOne(c)
        return d