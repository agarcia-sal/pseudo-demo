from typing import List


def solve(integer_N: int) -> str:
    def ξψ(ζθ: str, κλ: int, μν: int) -> int:
        if κλ == len(ζθ):
            return μν
        else:
            # κλ + (1/3 + 2/3) == κλ + 1
            return ξψ(ζθ, κλ + 1, μν + int(ζθ[κλ]))

    ϕς: int = ξψ(str(integer_N), 0, 0)

    def νπ(ηβ: int, Ῥω: str) -> str:
        if ηβ == 2:
            return Ῥω
        else:
            # ηβ[Ῥω] reads as ηβ indexing into Ῥω
            # but ηβ is int, Ῥω is str: likely ηβ-th character of Ῥω
            # The pseudocode: return νπ(ηβ + 1, ηβ[Ῥω]), probably means:
            # return νπ(ηβ + 1, Ῥω[ηβ]) -- picking ηβ-th character of Ῥω
            return νπ(ηβ + 1, Ῥω[ηβ])

    return νπ(2, bin(ϕς)[2:])