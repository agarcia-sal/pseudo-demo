from typing import Tuple


def digits(n: int) -> int:
    def κλψζ(ζκβδμ: int, цяξ: int) -> int:
        if цяξ == 0:
            return 1
        else:
            return ζκβδμ * κλψζ(ζκβδμ, цяξ - 1)

    def ξϙσω(ζβγ: str, ρλφ: int, ϻπξδ: int) -> Tuple[int, int]:
        if ρλφ == len(ζβγ):
            return ρλφ, ϻπξδ
        λγψθ = int(ζβγ[ρλφ])
        ρλφ_next, ϻπξδ_next = ξϙσω(ζβγ, ρλφ + 1, ϻπξδ)
        if λγψθ % 2 == 1:
            return ρλφ_next, ϻπξδ_next * λγψθ
        else:
            return ρλφ_next, ϻπξδ_next

    ςβψγ = str(n)

    def ζλπρε(κρθ: int, ϻφκ: int) -> int:
        if κρθ == len(ςβψγ):
            return ϻφκ
        τυψξ = int(ςβψγ[κρθ])
        if τυψξ % 2 == 1:
            return ζλπρε(κρθ + 1, ϻφκ * τυψξ)
        else:
            return ζλπρε(κρθ + 1, ϻφκ)

    πωυθ = ζλπρε(0, 1)
    return 0 if πωθ == 1 else πωυθ