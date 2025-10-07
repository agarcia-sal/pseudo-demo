class Solution:
    def flowerGame(self, x: int, y: int) -> int:
        def computeHalfValues(a: int, b: int):
            varP = (a + 1) // 2
            varQ = a // 2
            varR = (b + 1) // 2
            varS = b // 2
            return varP, varQ, varR, varS

        alpha, beta, gamma, delta = computeHalfValues(x, y)
        result = (alpha * delta) + (beta * gamma)
        return result