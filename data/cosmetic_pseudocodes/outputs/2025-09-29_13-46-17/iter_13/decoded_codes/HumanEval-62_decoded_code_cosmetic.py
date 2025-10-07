from typing import List

def derivative(list_of_coefficients: List[float]) -> List[float]:
    def wƹƉ𝔹(πṗ_: List[float], Ʒ₉: int) -> List[float]:
        if Ʒ₉ < len(πṗ_):
            return [πṗ_[Ʒ₉] * Ʒ₉] + wƹƉ𝔹(πṗ_, Ʒ₉ + 1)
        else:
            return []
    return wƹƉ𝔹(list_of_coefficients, 1)