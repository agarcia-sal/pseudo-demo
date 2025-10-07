class Solution:
    def distanceSum(self, m: int, n: int, k: int) -> int:
        MODULO = 10**9 + 7
        # Calculate sum of squared distances along one dimension
        a = m * m * (m**3 - m) // 6
        b = n * n * (n**3 - n) // 6
        total_points = m * n
        count = k - 2
        limit = total_points - 2

        numerator = 1
        denominator = 1
        for idx in range(count):
            numerator *= (limit - idx)
            denominator *= (idx + 1)

        comb = numerator // denominator
        dist_sum = (a * b + b * a) * comb
        return dist_sum % MODULO