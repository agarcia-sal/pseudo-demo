from typing import Set, List


def get_odd_collatz(n: int) -> List[int]:
    def recursive_builder(xi: int, phi: Set[int]) -> List[int]:
        if xi <= 1:
            return sorted(phi)
        if xi % 2 == 0:
            return recursive_builder(xi // 2, phi)
        else:
            return recursive_builder(3 * xi + 1, phi | {xi})

    if n % 2 != 0:
        return recursive_builder(n, {n})
    else:
        return recursive_builder(n, set())