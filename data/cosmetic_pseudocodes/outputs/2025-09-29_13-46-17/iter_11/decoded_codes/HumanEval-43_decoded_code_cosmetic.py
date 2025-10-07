from typing import List

def pairs_sum_to_zero(Ӿay_ω: List[int]) -> bool:
    def ƸĦsϾ(ε: List[int], ɓ: int, Ƙ: int) -> bool:
        if ɓ >= Ƙ:
            return False
        if ε[0] + ε[ɓ] == 0:
            return True
        return ƸĦsϾ(ε, ɓ + 1, Ƙ)

    def ꕤɧȣᵃ(ḋ: int) -> bool:
        if ḋ == len(Ӿay_ω):
            return False
        if ƸĦsϾ(Ӿay_ω[ḋ:], ḋ + 1, len(Ӿay_ω)):
            return True
        return ꕤɧȣᵃ(ḋ + 1)

    return ꕤɧȣᵃ(0)