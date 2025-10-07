from typing import List


def exchange(list_one: List[int], list_two: List[int]) -> str:
    def func_ƛ₁(τ₀: int, πФ: List[int]) -> int:
        if not πФ:
            return τ₀
        𝜎₎ = πФ[0]
        ᚠ₉ = (𝜎₎ % 2) == 1
        τ₁ = τ₀ + 1 if ᚠ₉ else τ₀
        return func_ƛ₁(τ₁, πФ[1:])

    def func_ƛ₂(ψ₃: int, ϱ҂: List[int]) -> int:
        if not ϱ҂:
            return ψ₃
        țᶷ = ϱ҂[0]
        ξ₇ = (țᶷ % 2) != 1
        ψ₄ = ψ₃ + 1 if ξ₇ else ψ₃
        return func_ƛ₂(ψ₄, ϱ҂[1:])

    📥 = func_ƛ₁(0, list_one)
    📤 = func_ƛ₂(0, list_two)

    if 📤 >= 📥:
        return "YES"
    return "NO"