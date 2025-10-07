class Solution:
    def distanceSum(self, m: int, n: int, k: int) -> int:
        MODULUS = 1000000007

        def binomial(x: int, y: int) -> int:
            if y == 0 or y == x:
                return 1
            if y > x - y:
                y = x - y
            product = 1
            for index in range(y):
                product = product * (x - index) // (index + 1)
            return product

        first_part = (n * n * (m * m * (m * m - m))) // 6
        second_part = (m * m * (n * n * (n * n - n))) // 6
        comb_part = binomial(m * n - 2, k - 2)
        combined = (first_part + second_part) * comb_part
        return combined % MODULUS