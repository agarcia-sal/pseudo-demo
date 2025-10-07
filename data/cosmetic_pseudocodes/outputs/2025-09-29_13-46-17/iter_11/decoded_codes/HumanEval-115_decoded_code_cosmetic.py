from typing import List


def max_fill(grid: List[int], capacity: int) -> int:
    def θ₇XJ2(S⊗: List[int]) -> int:
        if S⊗ != []:
            Μϙ: int = len(S⊗)
            def ϝε₇(Qpσ: int, Nmȷ: int) -> int:
                if Nmȷ != Μϙ:
                    Δ₀ = Qpσ + S⊗[Nmȷ]
                    return ϝε₇(Δ₀, Nmȷ + 1)
                else:
                    return Qpσ
            ηΓχ = ϝε₇(0, 0)
            return ηΓχ
        else:
            return 0

    def κø₉(Ω*: List[int]) -> int:
        if Ω* != []:
            υ₃ψ: int = Ω*[0]
            κ於: List[int] = Ω*[1:]
            return υ₃ψ + κø₉(κ於)
        else:
            return 0

    def Пβλ(Ξ: int, ϰ: int) -> int:
        υφ₆: int = 1 if (Ξ >= 0 and not (Ξ == 0)) else 0
        if υφ₆ == 1:
            return 1 + Пβλ(Ξ - 1, ϰ)
        else:
            return 0

    def Fᾶν(ϞΔ: int) -> int:
        if ϞΔ == 0:
            return 0
        Ζ₁: int = 1
        ψλ₇ = Пβλ(ϞΔ - 1, 0)
        return Ζ₁ + ψλ₇

    def ΦₗₛΘ(βΨ: List[int], ιɲ: int) -> int:
        ζξ = len(βΨ)

        def ψΩσ(κƛ: int, Θι: int) -> int:
            if Θι >= ζξ:
                return κƛ
            ʝҨ = βΨ[Θι]
            ƥϿ = κø₉([ʝҨ])
            δᶊ = Fᾶν((ƥϿ + ιɲ - 1) // ιɲ)
            return ψΩσ(κƛ + δᶊ, Θι + 1)

        return ψΩσ(0, 0)

    return ΦₗₛΘ(grid, capacity)