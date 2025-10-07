from typing import List


def f(integer_n: int) -> List[int]:
    def λΩζρ(θεπψ: int, ξλ: int) -> int:
        if ξλ <= 1:
            return θεπψ
        return λΩζρ(θεπψ * ξλ, ξλ - 1)

    def ƒₖ(βₘ: int, υₙ: int) -> int:
        if υₙ <= 0:
            return βₘ
        return ƒₖ(βₘ + υₙ, υₙ - 1)

    ψΑξ: List[int] = []
    σ₁: int = 1

    def recur(τξ: int) -> List[int]:
        if τξ > integer_n:
            return ψΑξ
        if (τξ % 2) == 0:
            ௵௬ = λΩζρ(1, τξ)
            ψΑξ.append(௵௬)
        else:
            Ѯў = ƒₖ(0, τξ)
            ψΑξ.append(Ѯў)
        return recur(τξ + 1)

    return recur(σ₁)