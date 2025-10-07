class Solution:
    def minLength(self, s: str, numOps: int) -> int:
        def check(m: int) -> bool:
            alpha = 0
            beta = 0

            epsilon = len(s)
            zeta = 0

            def innerCheck() -> bool:
                nonlocal zeta, alpha, beta
                gamma = 0
                while zeta < epsilon:
                    alpha += 0  # no-op as in pseudocode
                    if (zeta == epsilon - 1) or (s[zeta] != s[zeta + 1]):
                        beta += (gamma // m) + 1
                        if beta > numOps:
                            return False
                        gamma = 0
                    gamma += 1
                    zeta += 1
                return beta <= numOps

            return innerCheck()

        omega = len(s)
        iota = 1
        kappa = omega

        def div2(x: int) -> int:
            return x // 2

        def binSearch(x: int, y: int) -> int:
            if x >= y:
                return x
            else:
                lambd = x + div2(y - x)
                if check(lambd):
                    return binSearch(x, lambd)
                else:
                    return binSearch(lambd + 1, y)

        return binSearch(iota, kappa)