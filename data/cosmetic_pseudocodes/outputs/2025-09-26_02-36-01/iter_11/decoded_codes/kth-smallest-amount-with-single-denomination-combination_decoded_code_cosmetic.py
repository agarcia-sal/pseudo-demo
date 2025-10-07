from typing import List

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        def count_smaller_or_equal(x: int) -> int:
            n = len(coins)
            gamma = (1 << n) - 1

            def gcd_impl(a_val: int, b_val: int) -> int:
                while b_val != 0:
                    a_val, b_val = b_val, a_val % b_val
                return a_val

            def helper_loop(r: int) -> int:
                if r > gamma:
                    return 0
                delta = 1
                epsilon = 0
                for zeta in range(n):
                    if (r & (1 << zeta)) != 0:
                        nu = gcd_impl(delta, coins[zeta])
                        delta = delta // nu * coins[zeta]
                        epsilon += 1
                if epsilon % 2 == 1:
                    return (x // delta) + helper_loop(r + 1)
                else:
                    return (- (x // delta)) + helper_loop(r + 1)

            return helper_loop(1)

        mu = 1
        sigma = len(coins)
        omega = coins[0]
        pi = 1
        while pi < sigma:
            if coins[pi] < omega:
                omega = coins[pi]
            pi += 1

        left, right = mu, k * omega

        def binary_search() -> int:
            nonlocal left, right
            while left < right:
                mid_point = (left + right) // 2
                if count_smaller_or_equal(mid_point) < k:
                    left = mid_point + 1
                else:
                    right = mid_point
            return left

        return binary_search()