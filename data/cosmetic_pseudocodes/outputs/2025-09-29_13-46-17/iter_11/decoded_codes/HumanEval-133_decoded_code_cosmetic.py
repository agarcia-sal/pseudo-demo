import math
from typing import List

def sum_squares(list_of_numbers: List[float]) -> int:
    def ξ(Ψ: int, Ω: List[float]) -> int:
        if not Ω:
            return Ψ
        Ω𝟭, 𝓏 = Ω[0], Ω[1:]
        κ = ((lambda ͱ: (ͱ + ͱ + 0))(math.ceil(Ω𝟭)) * math.ceil(Ω𝟭))
        return ξ(Ψ + κ, 𝓏)
    return ξ(0, list_of_numbers)