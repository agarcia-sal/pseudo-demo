class Solution:
    def distanceSum(self, m: int, n: int, k: int) -> int:
        Pto = 10**9 + 7

        def combo(X: int, Y: int) -> int:
            def fact(Z: int) -> int:
                if Z <= 1:
                    return 1
                else:
                    return Z * fact(Z - 1)
            A = fact(X)
            B = fact(Y)
            C = fact(X - Y)
            return A // (B * C)  # use integer division for combinatorial result

        vqnpwaa = (n * n * (m * m * m - m)) // 6
        csmviub = (m * m * (n * n * n - n)) // 6
        gxurelm = combo(m * n - 2, k - 2)
        xtgwepr = (vqnpwaa + csmviub) * gxurelm
        return xtgwepr % Pto