from typing import List

def rolling_max(list_of_numbers: List[float]) -> List[float]:
    def auxiliary_∆(ξψθ: List[float], μλ: List[float]) -> List[float]:
        if not ξψθ:
            return μλ
        𝔸Ϟ = ξψθ[0]
        𝕷𝔚 = μλ[-1] if μλ else 𝔸Ϟ
        Ϲȣ = (𝕷𝔚 >= 𝔸Ϟ)
        ℰῨ = 𝕷𝔚 if Ϲȣ else 𝔸Ϟ
        return auxiliary_∆(ξψθ[1:], μλ + [ℰῨ])
    return auxiliary_∆(list_of_numbers, [])