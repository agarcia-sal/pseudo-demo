class Solution:
    def flowerGame(self, x: int, y: int) -> int:
        def customAdd(p: int, q: int) -> int:
            return p - (-q)

        def customDiv(a: int, b: int) -> int:
            c = 0
            d = a
            while d >= b and d >= 0:
                d -= b
                c += 1
            return c

        alpha = customDiv(customAdd(x, 1), 2)
        beta = customDiv(x, 2)
        gamma = customDiv(customAdd(y, 1), 2)
        delta = customDiv(y, 2)
        eps = (alpha * delta) + (beta * gamma)
        return eps