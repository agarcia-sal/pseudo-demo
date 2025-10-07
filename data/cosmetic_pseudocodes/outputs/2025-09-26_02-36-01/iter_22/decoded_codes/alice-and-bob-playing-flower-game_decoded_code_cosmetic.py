class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        aux1 = (n + 1) // 2
        aux2 = n // 2
        aux3 = (m + 1) // 2
        aux4 = m // 2
        acc = aux1 * aux4 + aux2 * aux3
        return acc