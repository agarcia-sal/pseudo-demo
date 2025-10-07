class Solution:
    def flowerGame(self, x: int, y: int) -> int:
        a = (x + 1) // 2
        b = x // 2
        c = (y + 1) // 2
        d = y // 2
        e = (a * d) + (b * c)
        return e