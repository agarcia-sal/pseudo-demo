class Solution:
    def distanceSum(self, m: int, n: int, k: int) -> int:
        MODULUS = 10**9 + 7

        def computeCombinations(x: int, y: int) -> int:
            if y > x:
                return 0
            if y == 0:
                return 1
            pascal = [[0] * (y + 1) for _ in range(x + 1)]
            for i in range(x + 1):
                limit = min(i, y)
                for j in range(limit + 1):
                    if j == 0 or j == i:
                        pascal[i][j] = 1
                    else:
                        pascal[i][j] = (pascal[i - 1][j - 1] + pascal[i - 1][j]) % MODULUS
            return pascal[x][y]

        def integerPower(base: int, exponent: int) -> int:
            result = 1
            tempBase = base % MODULUS
            tempExp = exponent
            while tempExp > 0:
                if tempExp % 2 == 1:
                    result = (result * tempBase) % MODULUS
                tempBase = (tempBase * tempBase) % MODULUS
                tempExp //= 2
            return result

        def calcPart(largeVal: int, smallVal: int) -> int:
            # Compute (smallVal^2 * (largeVal * (largeVal^2 - 1)/6)) mod MODULUS
            # Use pow for clarity, integer division guaranteed since largeVal*(largeVal^2 -1) divisible by 6 for integer largeVal
            largeVal_cubed_minus_one = (pow(largeVal, 3, MODULUS) - largeVal) % MODULUS  # largeVal^3 - largeVal mod MOD
            # The division by 6 is exact in integer arithmetic for the original expression, but modulo inverse needed here
            # However, since MODULUS is prime, multiply by inverse of 6 mod MODULUS instead of integer division
            inv_6 = pow(6, MODULUS - 2, MODULUS)  # Modular inverse of 6 modulo MODULUS

            part = (smallVal * smallVal) % MODULUS
            part = (part * largeVal) % MODULUS
            part = (part * largeVal_cubed_minus_one) % MODULUS
            part = (part * inv_6) % MODULUS
            return part

        a = m
        b = n
        part1 = calcPart(b, a)
        part2 = calcPart(a, b)
        totalElements = a * b
        combinationsCount = computeCombinations(totalElements - 2, k - 2)
        tempSum = ((part1 + part2) % MODULUS) * combinationsCount
        answer = tempSum % MODULUS
        return answer