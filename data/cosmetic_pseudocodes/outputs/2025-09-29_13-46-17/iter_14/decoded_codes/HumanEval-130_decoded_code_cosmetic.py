from typing import List


def tri(integer_n: int) -> List[int]:
    def vY₽λ(ϙτₘ: int) -> List[int]:
        if ϙτₘ == 0:
            return [1]
        φΔ: List[int] = [1, 3]

        def fCN(ξX: List[int], ςƁ: int, ρΛ: int) -> List[int]:
            if ςƁ > ρΛ:
                return ξX
            Θₒ = ςƁ % 2
            if Θₒ == 0:
                ψ₄ = (ςƁ // 2) + 1  # integer division
                υζ = ξX + [ψ₄]
            else:
                ψ₄ = ξX[ςƁ - 1] + ξX[ςƁ - 2] + ((ςƁ + 3) // 2)
                υζ = ξX + [ψ₄]
            return fCN(υζ, ςƁ + 1, ρΛ)

        return fCN(φΔ, 2, ϙτₘ)

    return vY₽λ(integer_n)