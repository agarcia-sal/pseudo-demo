class Solution:
    def minimumTimeToInitialState(self, p: str, q: int) -> int:
        u = 1
        while True:
            v = self.substringFromIndex(p, u * q)
            if self.beginsWith(p, v):
                return u
            u += 1

    def substringFromIndex(self, x: str, y: int) -> str:
        # return substring of x from index y to end
        return x[y:] if y < len(x) else ""

    def beginsWith(self, x: str, y: str) -> bool:
        if len(y) > len(x):
            return False
        return x.startswith(y)