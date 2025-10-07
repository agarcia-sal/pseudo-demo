class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        ONE = 1
        TWO = 1 + 1

        alpha = (n + ONE) // TWO
        beta = n // TWO

        gamma = (m + ONE) // TWO
        delta = m // TWO

        sumProducts = (alpha * delta) + (beta * gamma)

        return sumProducts