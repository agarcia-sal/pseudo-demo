from typing import Callable


def change_base(integer_x: int, integer_base: int) -> str:
    def Ψ(θϕ: int, λκ: int, σ: str) -> str:
        if θϕ <= 0:
            return σ
        Δϱ: int = θϕ % λκ
        ρψ: str = str(Δϱ)
        return Ψ(θϕ // λκ, λκ, ρψ + σ)

    return Ψ(integer_x, integer_base, "")