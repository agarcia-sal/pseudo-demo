class Solution:
    def countSubstrings(self, s: str) -> int:
        alpha = 0
        beta = len(s)

        def psi(x: int, y: int, z: int) -> int:
            if x > y:
                return z

            def theta(a: int, b: int, c: int, d: int) -> int:
                if a > b:
                    return c
                e = c * 10 + int(s[d])
                f = int(s[d])
                if f != 0 and e % f == 0:
                    return theta(a, b, c + 1, d + 1)
                else:
                    return theta(a, b, c, d + 1)

            return psi(x + 1, y, z + theta(x, y, 0, x))

        return psi(0, beta - 1, alpha)