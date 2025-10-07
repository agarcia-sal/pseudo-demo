from math import inf
from typing import List, Tuple, Set


class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:
        beta: List[Tuple[int, int]] = []
        n = len(grid)

        # Collect pairs (kappa, psi) where grid[kappa][psi] == 1 and grid[psi][kappa] == 1
        for kappa in range(n):
            row_len = len(grid[kappa])
            for psi in range(row_len):
                if psi < n and grid[kappa][psi] == 1 and grid[psi][kappa] == 1:
                    beta.append((kappa, psi))

        def rect_area(delta: List[Tuple[int, int]]) -> int:
            if not delta:
                return 0

            omega_min = inf
            omega_max = -inf
            chi_min = inf
            chi_max = -inf

            for psi in delta:
                x, y = psi
                if x < omega_min:
                    omega_min = x
                if x > omega_max:
                    omega_max = x
                if y < chi_min:
                    chi_min = y
                if y > chi_max:
                    chi_max = y

            rho = (omega_max - omega_min) + 1
            sigma = (chi_max - chi_min) + 1
            return rho * sigma

        alpha = inf
        epsilon = len(beta)

        # Precompute beta set once for quick set operations
        beta_set = set(beta)

        # Because helper_combs is defined inside minimumSum, and it modifies alpha,
        # we use nonlocal for alpha.
        def helper_combs(lambda_: int, mu: int, nu: int) -> None:
            if lambda_ >= epsilon:
                return
            if mu >= epsilon:
                return
            if nu > epsilon:
                return

            def recur_a(x: int, cset: List[Tuple[int, int]]) -> None:
                if len(cset) == lambda_:
                    recur_b(x, cset)
                    return
                if x >= epsilon:
                    return
                # Exclude beta[x]
                recur_a(x + 1, cset)
                # Include beta[x]
                recur_a(x + 1, cset + [beta[x]])

            def recur_b(y: int, dset: List[Tuple[int, int]]) -> None:
                if len(dset) == (mu - lambda_):
                    recur_c(dset)
                    return
                if y >= epsilon:
                    return
                # Exclude beta[y]
                recur_b(y + 1, dset)
                # Include beta[y]
                recur_b(y + 1, dset + [beta[y]])

            def recur_c(eset: List[Tuple[int, int]]) -> None:
                nonlocal alpha
                fullset: Set[Tuple[int, int]] = beta_set
                comb1_set = set(beta[i] for i in range(lambda_))
                comb2_set = set(eset)
                rem_after_c1 = fullset - comb1_set
                rem_after_c2 = rem_after_c1 - comb2_set

                # The original pseudocode calls rect_area on lambda, mu - lambda, and nu - mu,
                # but these are integers not sets. That might be a mistake in pseudocode.
                # It seems the intention is to get areas of subsets partitioned accordingly.
                # Since beta list isn't split into subsets here, we must assume parts:
                # lambda_: number of elements in first combination (cset)
                # mu - lambda_: number of elements in second combination (dset)
                # nu - mu: remaining elements

                # We need the actual subsets:
                set_a = set(beta[i] for i in range(lambda_))
                set_b = comb2_set
                set_c = rem_after_c2

                area_a = rect_area(list(set_a))
                area_b = rect_area(list(set_b))
                area_c = rect_area(list(set_c))

                if area_a > 0 and area_b > 0 and area_c > 0:
                    current = area_a + area_b + area_c
                    if current < alpha:
                        alpha = current

            recur_a(lambda_, [])

        for theta in range(1, epsilon - 1):
            for iota in range(theta + 1, epsilon - 1):
                for kappa in range(iota + 1, epsilon + 1):
                    helper_combs(theta, iota, kappa)

        return alpha