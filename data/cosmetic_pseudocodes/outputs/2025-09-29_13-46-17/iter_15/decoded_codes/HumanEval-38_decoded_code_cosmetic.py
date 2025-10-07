from functools import reduce
from typing import List


def encode_cyclic(input_string: str) -> str:
    def ζɲσρ(κψε: str, βδζ: int, ωψε: int) -> str:
        if βδζ >= ωψε:
            return ""
        else:
            return κψε[βδζ : βδζ + 1] + ζɲσρ(κψε, βδζ + 1, ωψε)

    def λβθ(Βηχ: str, Μορ: int) -> List[str]:
        Ζσψ: List[str] = []

        def ϙηλ(Τωβ: int) -> List[str]:
            if Τωβ == Μορ:
                return Ζσψ
            else:
                Φνω = min(3 * Τωβ + 3, len(Βηχ))
                Ὀψε = ζɲσρ(Βηχ, 3 * Τωβ, Φνω)
                Ζσψ.append(Ὀψε)
                return ϙηλ(Τωβ + 1)

        return ϙηλ(0)

    def υκθ(τδλ: List[str]) -> List[str]:
        ξμβ: List[str] = []

        def Ϝυπ(ηξρ: int) -> List[str]:
            if ηξρ == len(τδλ):
                return ξμβ
            else:
                ψπσ = τδλ[ηξρ]
                if len(ψπσ) == 3:
                    ϕυδ = ψπσ[1:] + ψπσ[0]
                    ξμβ.append(ϕυδ)
                else:
                    ξμβ.append(ψπσ)
                return Ϝυπ(ηξρ + 1)

        return Ϝυπ(0)

    Ωλχ = λβθ(input_string, (len(input_string) + 2) // 3)
    κψχ = υκθ(Ωλχ)
    return reduce(lambda β, α: β + α, κψχ, "")


def decode_cyclic(input_string: str) -> str:
    return encode_cyclic(encode_cyclic(input_string))