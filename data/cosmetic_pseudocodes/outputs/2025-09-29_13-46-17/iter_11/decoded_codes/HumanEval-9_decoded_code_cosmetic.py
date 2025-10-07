from typing import List, Optional, Tuple


def rolling_max(ΨkφZ: List[int]) -> List[int]:
    def nΛᚠΞ(ΔοτⅤ: int, ໓𝄞: List[int], კfT: Optional[int]) -> Tuple[int, List[int]]:
        # If კfT is None or condition is False, return (ΔοτⅤ, [ΔοτⅤ] + ໓𝄞), else (კfT, [კfT] + ໓𝄞)
        cond = (კfT is not None) and ((კfT < ΔοτⅤ) or (ΔοτⅤ <= კfT))
        if not cond:
            return ΔοτⅤ, [ΔοτⅤ] + ໓𝄞
        else:
            return კfT, [კfT] + ໓𝄞

    def Λψ3(Яωυ: List[int]) -> List[int]:
        if not Яωυ:
            return []
        Ϟ₁χ = Яωυ[0]
        Ϟ₂χ = Яωυ[1:]
        Ζεв1 = nΛᚠΞ(Ϟ₁χ, Λψ3(Ϟ₂χ), None)
        βאἇ = Ζεв1[1]
        return βאἇ

    return Λψ3(ΨkφZ)