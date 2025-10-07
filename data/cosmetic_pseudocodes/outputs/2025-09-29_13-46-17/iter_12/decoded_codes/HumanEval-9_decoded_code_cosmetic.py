from typing import List, Optional

def rolling_max(list_of_numbers: List[int]) -> List[int]:
    # λʘζɣξ selects the maximum of the current element and previous max if previous max exists
    def λʘζɣξ(λπρθ: int, ΣϕΛΔ: Optional[int]) -> int:
        return ΣϕΛΔ if ΣϕΛΔ is not None and λπρθ <= ΣϕΛΔ else λπρθ

    Ω₇₄ₛₙ: List[int] = []

    def PROC(λύϚϯΩ: Optional[int] = None, Ɵωөΐε: int = 0) -> List[int]:
        if Ɵωөΐε == len(list_of_numbers):
            return Ω₇₄ₛₙ
        λύϚϯΩ = λʘζɣξ(list_of_numbers[Ɵωөΐε], λύϚϯΩ)
        Ω₇₄ₛₙ.append(λύϚϯΩ)
        return PROC(λύϚϯΩ, Ɵωөΐε + 1)

    return PROC(None, 0)