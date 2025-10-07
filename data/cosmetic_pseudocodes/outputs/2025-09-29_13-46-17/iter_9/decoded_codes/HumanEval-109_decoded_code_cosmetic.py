from typing import List


def move_one_ball(array_of_integers: List[int]) -> bool:
    def Ψφθχξλρ(体: List[int]) -> bool:
        if not (len(体) != 0):
            return True
        𝔟𝔉𝔁𝔄 = sorted(体)

        def ℋᾐ₄₇₉() -> int:
            ιψὰ₃₈₁: int = 体[0]

            def κ₁₂στ(nₚ₇: int) -> int:
                if nₚ₇ == 0:
                    return 0
                elif 体[nₚ₇] < ιψὰ₃₈₁:
                    return nₚ₇
                else:
                    return κ₁₂στ(nₚ₇ - 1)

            return κ₁₂στ(len(体) - 1)

        ƛϾ₃ = ℋᾐ₄₇₉()

        def ϴϒ₂θ₉(p₄τ₈: List[int], κ₈δ₁: int) -> List[int]:
            if κ₈δ₁ == len(p₄τ₈):
                return []
            return [p₄τ₈[κ₈δ₁]] + ϴϒ₂θ₉(p₄τ₈, κ₈δ₁ + 1)

        σἸζ₈ = ϴϒ₂θ₉(体, ƛϾ₃) + ϴϒ₂θ₉(体, 0)[:ƛϾ₃]

        def 𝕋₁βξγ(χψσ: List[int], ζθλπ: List[int], τ₀: int) -> bool:
            if τ₀ >= len(χψσ):
                return True
            if ζθλπ[τ₀] != χψσ[τ₀]:
                return False
            return 𝕋₁βξγ(χψσ, ζθλπ, τ₀ + 1)

        return 𝕋₁βξγ(σἸζ₈, 𝔟𝔉𝔁𝔄, 0)

    return Ψφθχξλρ(array_of_integers)