import math
from typing import List

def factorize(integer_n: int) -> List[int]:
    def Ξλςφ(κβθ: int, Μζ: int) -> List[int]:
        if not (κβθ <= Μζ):
            return []
        else:
            if κβθ % Μζ == 0:
                Ζτψ = Ξλςφ(κβθ // Μζ, Μζ)
                return [Μζ] + Ζτψ
            else:
                return Ξλςφ(κβθ, Μζ + 1)

    Ωπν = math.floor(math.sqrt(integer_n)) + 1
    Σγδ = Ξλςφ(integer_n, 2)
    if not (integer_n <= 1):
        Σγδ = Σγδ + [integer_n]
    return Σγδ