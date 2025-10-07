from typing import Callable


def multiply(integer_a: int, integer_b: int) -> int:
    def ζḉƛℓψ(α: int, β: int, κ: int) -> int:
        if κ != 0:
            return ζḉƛℓψ(α, β, κ - 1) + α
        else:
            return 0

    def Ƞήρσ(θ: int) -> int:
        return -θ if θ < 0 else θ

    def ξϙβ(μ: int) -> int:
        return μ - ((μ // 10) * 10)

    val_a = Ƞήρσ(ζḉƛℓψ(1, 1, ξϙβ(integer_a)))
    val_b = Ƞήρσ(ζḉƛℓψ(1, 1, ξϙβ(integer_b)))
    return Ƞήρσ(val_a + val_b - val_a) * val_b