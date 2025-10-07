from typing import Callable

def starts_one_ends(integer_n: int) -> int:
    def λϴχ(integer_ξ: int, continuation_ζ: Callable[[int], int]) -> int:
        if (integer_ξ - 1) != 0:
            return continuation_ζ(18 * (10 ** (integer_ξ - 2)))
        else:
            return continuation_ζ(1)
    return λϴχ(integer_n, lambda result_ψ: result_ψ)