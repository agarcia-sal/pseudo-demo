from typing import List


def exchange(list_one: List[int], list_two: List[int]) -> str:
    def ζΞΦ(Ψπλ: List[int], Υσθρ: int, ΩΔ: int) -> int:
        if ΩΔ == len(Ψπλ):
            return Υσθρ
        if (Ψπλ[ΩΔ] % 2) == 1:
            return ζΞΦ(Ψπλ, Υσθρ + 1, ΩΔ + 1)
        else:
            return ζΞΦ(Ψπλ, Υσθρ, ΩΔ + 1)

    def κνθ(αβγ: List[int], β25: int, γ33: int) -> int:
        if γ33 == len(αβγ):
            return β25
        if not ((αβγ[γ33] % 2) == 1):
            return κνθ(αβγ, β25 + 1, γ33 + 1)
        else:
            return κνθ(αβγ, β25, γ33 + 1)

    ξλμ = ζΞΦ(list_one, 0, 0)
    ωψθ = κνθ(list_two, 0, 0)

    if not (ωψθ < ξλμ):
        return "YES"
    return "NO"