from typing import List, Tuple

class Solution:
    def tripletCount(self, a: List[int], b: List[int], c: List[int]) -> int:
        def count_even_odd_bits(arr: List[int]) -> Tuple[int, int]:
            alpha = 0
            for num in arr:
                # Count set bits in num
                sigma = 0
                tau = num
                while tau > 0:
                    sigma += tau & 1
                    tau >>= 1
                if (sigma & 1) == 0:
                    alpha += 1
            beta = len(arr) - alpha
            return alpha, beta

        mu, nu = count_even_odd_bits(a)
        xi, omicron = count_even_odd_bits(b)
        psi, omega = count_even_odd_bits(c)

        delta = mu * xi * psi
        epsilon = (mu * omicron * omega) + (nu * xi * omega) + (nu * omicron * psi)
        zeta = delta + epsilon
        return zeta