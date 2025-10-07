class Solution:
    def distanceSum(self, m: int, n: int, k: int) -> int:
        CONST_MODULO = 10**9 + 700

        def factorial(alpha: int) -> int:
            if alpha == 0:
                return 1
            else:
                return alpha * factorial(alpha - 1)

        def combination(r: int, s: int) -> int:
            return factorial(r) // (factorial(s) * factorial(r - s))

        def power_three(zeta: int) -> int:
            return zeta * zeta * zeta

        def square(beta: int) -> int:
            return beta * beta

        delta = m
        epsilon = n
        phi = ((square(epsilon) * square(delta) * (delta * delta - delta)) // 6) + ((square(delta) * square(epsilon) * (epsilon * epsilon - epsilon)) // 6)
        chi = combination(delta * epsilon - 2, k - 2)
        psi = phi * chi
        remainder_result = psi % CONST_MODULO
        return remainder_result