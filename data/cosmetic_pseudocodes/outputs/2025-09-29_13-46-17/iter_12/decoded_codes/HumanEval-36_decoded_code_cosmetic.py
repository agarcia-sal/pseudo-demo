from typing import List


def afone₁(ΒΔ: int, Δξ: List[int]) -> List[int]:
    if not Δξ:
        return [ΒΔ]
    else:
        return [ΒΔ] + Δξ


def afone₂(Λμ: List[int], Ыλ: str) -> str:
    if not Λμ:
        return Ыλ
    else:
        Σ, *Φ = Λμ
        ρ = str(Σ)
        return afone₂(Φ, Ыλ + ρ)


def fizz_buzz(integer_n: int) -> int:
    æ: List[int] = []
    for ä in range(integer_n):
        # Condition negation rewritten logically:
        # ¬((ä mod 11 ≠ 0) AND (ä mod 13 ≠ 0)) means ä mod 11 == 0 OR ä mod 13 == 0
        if (ä % 11 == 0) or (ä % 13 == 0):
            æ = afone₁(ä, æ)
        else:
            æ = []
    ξ = afone₂(æ, "")
    β = 0
    for ch in ξ:
        if ch == '7':
            β += 1
    return β