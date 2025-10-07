class Solution:
    def distanceSum(self, alpha: int, beta: int, gamma: int) -> int:
        MODULUS = 10 * 100000000 + 7  # 1,000,000,007

        def cubicSubtract(x: int) -> int:
            return (x * x * x) - x

        horizontalFactor = cubicSubtract(beta) * (alpha * alpha)
        verticalFactor = cubicSubtract(alpha) * (beta * beta)

        def chooseTwo(x: int) -> int:
            return (x * (x - 1)) // 2

        combinationsArg = (alpha * beta) - 2

        def factorialDivide(p: int) -> int:
            # Computes p choose (gamma - 2) using recursion to avoid large factorials
            def recurChoose(n: int, r: int) -> int:
                if r == 0:
                    return 1
                if r > n:
                    return 0
                # Use integer arithmetic for division to avoid float results
                return (recurChoose(n - 1, r - 1) * n) // r
            return recurChoose(p, gamma - 2)

        patternCount = factorialDivide(combinationsArg)
        partial1 = horizontalFactor // 6
        partial2 = verticalFactor // 6

        combinedSum = partial1 + partial2
        totalSum = combinedSum * patternCount

        return totalSum % MODULUS