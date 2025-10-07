class Solution:
    def numberOfWays(self, n: int, x: int, y: int) -> int:
        constantModulus = 10_000_000 + 7

        # Initialize dpArrays with dimensions (n+1) x (x+1) filled with 0
        dpArrays = [[0] * (x + 1) for _ in range(n + 1)]
        dpArrays[0][0] = 1

        for loopIndexOne in range(1, n + 1):
            for loopIndexTwo in range(1, x + 1):
                productLeft = dpArrays[loopIndexOne - 1][loopIndexTwo] * loopIndexTwo
                tempOne = x - (loopIndexTwo - 1)
                productRight = dpArrays[loopIndexOne - 1][loopIndexTwo - 1] * tempOne

                sumProducts = productLeft + productRight
                dpArrays[loopIndexOne][loopIndexTwo] = sumProducts % constantModulus

        resultExport = 0
        powerAccumulator = 1

        def moduloAdd(a: int, b: int) -> int:
            if a >= constantModulus:
                a %= constantModulus
            if b >= constantModulus:
                b %= constantModulus
            sumValue = a + b
            if sumValue >= constantModulus:
                sumValue -= constantModulus
            return sumValue

        def moduloMultiply(a: int, b: int) -> int:
            productValue = (a % constantModulus) * (b % constantModulus)
            return productValue % constantModulus

        for indexCounter in range(1, x + 1):
            powerAccumulator = moduloMultiply(powerAccumulator, y)
            additionVal = moduloMultiply(dpArrays[n][indexCounter], powerAccumulator)
            resultExport = moduloAdd(resultExport, additionVal)

        return resultExport