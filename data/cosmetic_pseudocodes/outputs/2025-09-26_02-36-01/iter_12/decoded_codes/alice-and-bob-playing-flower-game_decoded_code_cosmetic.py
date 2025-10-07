class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        def halfRoundedUp(x: int) -> int:
            return (x + 1) // 2

        def halfRoundedDown(x: int) -> int:
            return x // 2

        p = halfRoundedUp(n)
        q = halfRoundedDown(n)
        r = halfRoundedUp(m)
        s = halfRoundedDown(m)

        u = (p * s) + (q * r)
        return u