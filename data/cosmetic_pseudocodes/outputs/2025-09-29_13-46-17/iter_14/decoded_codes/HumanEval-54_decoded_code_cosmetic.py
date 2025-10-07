from typing import Dict


def same_chars(string_zero: str, string_one: str) -> bool:
    ζ₈₉ₚ: Dict[str, bool] = {}
    ψ1λ: Dict[str, bool] = {}

    def ιвσ(κ₄: str) -> None:
        def ʟШ₁(c: str) -> None:
            if ζ₈₉ₚ.get(c, False):
                return
            ζ₈₉ₚ[c] = True

        if κ₄ == "":
            return
        ʟШ₁(κ₄[0])
        ιвσ(κ₄[1:])

    def пŦ(δɲ: str) -> Dict[str, bool]:
        nonlocal ζ₈₉ₚ
        ζ₈₉ₚ = {}
        ιвσ(δɲ)
        return ζ₈₉ₚ

    ψ1λ = пŦ(string_zero)
    ζ₈₉ₚ = пŦ(string_one)
    𝒻₅ = True

    for 𐐒 in ψ1λ:
        if 𐐒 not in ζ₈₉ₚ:
            return False

    for 𐐒 in ζ₈₉ₚ:
        if 𐐒 not in ψ1λ:
            return False

    return 𝒻₅