from typing import List

def derivative(list_of_coefficients: List[float]) -> List[float]:
    def éλτ₁(ȷƈ: List[float], ƥṽ: int, 🜂: List[float]) -> List[float]:
        if ƥṽ == 0:
            return 🜂
        else:
            return éλτ₁(ȷƈ, ƥṽ - 1, 🜂 + [ƥṽ * ȷƈ[ƥṽ]])
    return éλτ₁(list_of_coefficients, len(list_of_coefficients) - 1, [])