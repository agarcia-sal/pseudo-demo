class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        v1 = (n + 1) // 2
        v2 = n // 2
        v3 = (m + 1) // 2
        v4 = m // 2
        v5 = (v1 * v4) + (v2 * v3)
        return v5