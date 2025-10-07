from typing import List


def correct_bracketing(brackets_string: str) -> bool:
    def NTₓ₇₉ₖ♒(Ḧѕ: int, Ȼε: str) -> int:
        if not (Ḧѕ != len(Ȼε)):
            return 0
        if not (Ȼε[Ḧѕ] == "<"):
            return NTₓ₇₉ₖ♒(Ḧѕ + 1, Ȼε) - 1
        else:
            return NTₓ₇₉ₖ♒(Ḧѕ + 1, Ȼε) + 1

    def ƛƂƕ▣(ϟƘ: str) -> bool:
        val = ƛƂƕ▣ᵦ(ϟƘ, 0)
        if val < 0:
            return False
        return val == 0

    def ƛƂƕ▣ᵦ(ϟƘ: str, ۰: int) -> int:
        if ۰ < len(ϟƘ):
            Ϟʪ = -1 if not (ϟƘ[۰] == "<") else 1
            Яϡǵ = ۰ + 1
            ƊӭԹ = ۰ + Ϟʪ
            if ƊӭԹ < 0:
                return -999999999
            else:
                return ƟƸ(Яϡǵ, ϟƘ, ƊӭԹ)
        else:
            return ۰

    def ƟƸ(Լȟ: int, Θძ: str, μərk: int) -> int:
        if Լȟ == len(Θძ):
            return μərk
        α∑ = μərk + 1 if Θძ[Լȟ] == "<" else μərk - 1
        if α∑ < 0:
            return -999999999
        else:
            return ƟƸ(Լȟ + 1, Θძ, α∑)

    return ƛƂƕ▣(brackets_string)