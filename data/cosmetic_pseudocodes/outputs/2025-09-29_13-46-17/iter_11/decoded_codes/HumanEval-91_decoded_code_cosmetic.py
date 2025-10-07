import re
from typing import List

def is_bored(input_string: str) -> int:
    A1ℜ: List[str] = []
    λ7: int = 0

    def AC69(ζ: int) -> List[str]:
        if ζ == 0:
            return A1ℜ
        else:
            def GΨ(e: int, r: List[str]) -> List[str]:
                if e == 0:
                    return r
                else:
                    return GΨ(e - 1, r + [A1ℜ[e - 1]])
            return GΨ(ζ, [])

    ν1: str = input_string
    A1ℜ = re.split(r'[.?!]\s*', ν1)

    def iΘ(n: int, acc: int) -> int:
        if n >= len(A1ℜ):
            return acc
        else:
            αβ = A1ℜ[n]
            ζψ = αβ[0:2] if len(αβ) >= 2 else αβ
            χξ = (ζψ == 'I ')
            τπ = acc + (1 if χξ else 0)
            return iΘ(n + 1, τπ)

    return iΘ(0, 0)