from typing import List, Tuple

class Solution:
    def tripletCount(self, a: List[int], b: List[int], c: List[int]) -> int:
        def count_even_odd_bits(arr: List[int]) -> Tuple[int, int]:
            even_count = 0
            odd_count = 0
            for num in arr:
                # Count set bits in num using Brian Kernighan’s algorithm
                count = 0
                n = num
                while n > 0:
                    n &= (n - 1)
                    count += 1
                if count % 2 == 0:
                    even_count += 1
                else:
                    odd_count += 1
            return even_count, odd_count

        epsilon_even, zeta_odd = count_even_odd_bits(a)
        eta_even, theta_odd = count_even_odd_bits(b)
        iota_even, kappa_odd = count_even_odd_bits(c)

        lambda_case1 = epsilon_even * eta_even * iota_even
        mu_case2 = (
            epsilon_even * theta_odd * kappa_odd +
            zeta_odd * eta_even * kappa_odd +
            zeta_odd * theta_odd * iota_even
        )
        pi_result = lambda_case1 + mu_case2

        return pi_result