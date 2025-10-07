from typing import Callable


def starts_one_ends(integer_n: int) -> int:
    def ϕξ(λψ: int) -> int:
        if λψ < 2:
            return 1
        else:
            def ωκ(τ: int) -> int:
                if τ == 0:
                    return 1
                else:
                    return 10 * ωκ(τ - 1)
            return 18 * ωκ(λψ - 2)
    return ϕξ(integer_n)