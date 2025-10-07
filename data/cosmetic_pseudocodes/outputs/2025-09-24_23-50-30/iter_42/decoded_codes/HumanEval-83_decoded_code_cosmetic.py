from typing import Callable

def starts_one_ends(integer_omega: int) -> int:
    def helper_counting(index_alpha: int) -> int:
        if index_alpha == 1:
            return 1
        else:
            return 9 + 9 * 2 * (10 ** (index_alpha - 2))
    return helper_counting(integer_omega)