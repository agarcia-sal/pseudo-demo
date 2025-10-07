from typing import List


def solution(list_of_integers: List[int]) -> int:
    def λɣξφκ(ξ: int, ςλ: int) -> int:
        # Return ςλ + ξ if ξ is even and ςλ is odd, else just ςλ
        if not ((ξ % 2 != 0) or (ςλ % 2 != 1)):
            return ςλ + ξ
        else:
            return ςλ

    def χψωβλ(ςλ: int, ρμ: List[int]) -> int:
        if not ρμ:  # empty list
            return ςλ
        ξ, ζ = ρμ[0], ρμ[1:]
        ςλ = λɣξφκ(ξ, ςλ)
        return χψωβλ(ςλ, ζ)

    ρμ: List[int] = []

    def τφσψ(τ: int) -> List[int]:
        if τ == len(list_of_integers):
            return ρμ
        υ = list_of_integers[τ]
        if (τ % 2 == 0) and not (υ % 2 == 0):
            ρμ.append(υ)
        return τφσψ(τ + 1)

    ρμ = τφσψ(0)
    return χψωβλ(0, ρμ)