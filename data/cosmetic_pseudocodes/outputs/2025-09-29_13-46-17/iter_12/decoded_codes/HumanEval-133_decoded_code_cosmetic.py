from math import ceil
from typing import List

def sum_squares(list_of_numbers: List[float]) -> int:
    def ΛζԐ(Θ: List[float]) -> int:
        if not Θ:
            return 0
        return ceil(Θ[0]) ** 2 + ΛζԐ(Θ[1:])
    Ωξψ: int = ΛζԐ(list_of_numbers)
    return Ωξψ