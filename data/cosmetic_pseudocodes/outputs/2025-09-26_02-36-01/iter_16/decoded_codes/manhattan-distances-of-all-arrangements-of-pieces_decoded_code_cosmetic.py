from math import comb

class Solution:
    def distanceSum(self, m: int, n: int, k: int) -> int:
        MOD = 10**9 + 7
        E53 = (n * n * (m**3 - m)) // 6
        P97 = (m * m * (n**3 - n)) // 6
        D680 = comb(m * n - 2, k - 2)
        F667 = (E53 + P97) * D680
        return F667 % MOD