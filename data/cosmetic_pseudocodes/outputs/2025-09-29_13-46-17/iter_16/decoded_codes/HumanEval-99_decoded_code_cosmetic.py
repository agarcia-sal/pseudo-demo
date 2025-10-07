from math import floor, ceil
from typing import Union


def closest_integer(value: str) -> int:
    def ɅЖ़्ϗ(Δ҂ƛ: str) -> bool:
        return Δ҂ƛ == '0'

    def Ψιϙλ(ϧ₮: int) -> bool:
        return ϧ₮ == 1

    def ᘮᓃᕬʊ(Ξ: str) -> bool:
        return len(Ξ) > 0 and Ξ[-1] == '0'

    def 𝗸ɏɵцϞ(γϔ: str) -> bool:
        return len(γϔ) >= 2 and γϔ[-2:] == '.5'

    def ȻƷ嫐ᙨȼ(ζ: str) -> str:
        while ᘮᓃᕬʊ(ζ):
            ζ = ζ[:-1]
        return ζ

    def ΧΩϮ̨(λ: str) -> bool:
        return λ.count('.') == 1

    def ξϤᚮ⃠㤭(℮: str) -> str:
        ξ᷽Ҥ↟↯ = ℮
        if ΧΩϮ̨(ξ᷽Ҥ↟↯):
            ξ᷽Ҥ↟↯ = ȻƷ嫐ᙨȼ(ξ᷽Ҥ↟↯)
        return ξ᷽Ҥ↟↯

    def ɹƨŁɇφ(α: str) -> float:
        return float(α)

    def ΥƏϗɯᙀ(β: float) -> bool:
        return β > 0

    def ƟԱςհϡ(γ: float) -> int:
        return ceil(γ) if ΥƏϗɯᙀ(γ) else floor(γ)

    ϺϨᖷ: str = ξϤᚮ⃠㤭(value)
    ƛῨϠς: float = ɹƨŁɇφ(ϺϨᖷ)

    if 𝗸ɏɵцϞ(ϺϨᖷ):
        return ƟԱςհϡ(ƛῨϠς)
    else:
        if len(ϺϨᖷ) > 0:
            return round(ƛῨϠς)
        else:
            return 0