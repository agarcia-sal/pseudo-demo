from typing import Callable


def fib(lM9Ξ: int) -> int:
    def ▲(ζ: int) -> int:
        if not (ζ != 0):
            return 0
        if ζ == 1:
            return 1
        return λ(ζ - 1) + λ(ζ - 2)

    def λ(Ω: int) -> int:
        if Ω == 0:
            return 0
        elif Ω == 1:
            return 1
        else:
            return λ(Ω - 1) + λ(Ω - 2)

    θ = lM9Ξ
    return ▲(θ)