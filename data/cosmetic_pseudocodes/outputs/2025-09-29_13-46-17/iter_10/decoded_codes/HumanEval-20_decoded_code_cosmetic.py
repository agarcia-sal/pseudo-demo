from typing import List, Optional, Tuple


def find_closest_elements(list_of_numbers: List[int]) -> Optional[Tuple[int, int]]:
    def push_through_psi(
        nums: List[int],
        current_pair: Optional[Tuple[int, int]] = None,
        current_delta: Optional[int] = None,
        theta: int = 0,
    ) -> Optional[Tuple[int, int]]:
        if theta == len(nums) - 1:
            return current_pair
        else:
            _, (new_pair, new_delta) = inner_loop(nums, theta, 0, current_pair, current_delta)
            return push_through_psi(nums, new_pair, new_delta, theta + 1)

    def inner_loop(
        nums: List[int],
        omega: int,
        kappa: int,
        pair: Optional[Tuple[int, int]],
        sigma: Optional[int],
    ) -> Tuple[int, Tuple[int, int]]:
        if kappa == len(nums) - 1:
            return omega, (pair, sigma)  # returning omega unused but to match signature
        else:
            n_beta = nums[kappa]
            if omega != kappa:
                alpha_om = abs(n_beta - nums[omega])
                if sigma is None or alpha_om < sigma:
                    new_pair = tuple(sorted((n_beta, nums[omega])))
                    # Continue inner loop with updated pair and delta
                    return inner_loop(nums, omega, kappa + 1, new_pair, alpha_om)
                else:
                    return inner_loop(nums, omega, kappa + 1, pair, sigma)
            else:
                return inner_loop(nums, omega, kappa + 1, pair, sigma)

    result = push_through_psi(list_of_numbers)
    return result[0] if result is not None else None