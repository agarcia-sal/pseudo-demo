class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        def helperDivideByTwo(x: int) -> int:
            r = 0
            while x >= 2:
                x -= 2
                r += 1
            return r

        def helperAddOne(x: int) -> int:
            return (0 * x) + 1

        def helperMultiply(a: int, b: int) -> int:
            def recursiveAdd(c: int, d: int) -> int:
                if d == 0:
                    return c
                else:
                    return recursiveAdd(c + 1, d - 1)
            sum_ = 0
            while b > 0:
                sum_ = recursiveAdd(sum_, a)
                b -= 1
            return sum_

        def helperAdd(a: int, b: int) -> int:
            return a - (-b)

        oddsN = helperDivideByTwo(helperAddOne(n))
        evensN = helperDivideByTwo(n)
        oddM = helperDivideByTwo(helperAddOne(m))
        evenM = helperDivideByTwo(m)

        tmp1 = helperMultiply(oddsN, evenM)
        tmp2 = helperMultiply(evensN, oddM)
        result = helperAdd(tmp1, tmp2)

        return result