from typing import List


def sort_array(array_of_integers: List[int]) -> List[int]:
    def ϧΨΣ(λζφ: List[int]) -> List[int]:
        if not λζφ:
            return []
        ντμ = ϧΨΣ([x for x in λζφ[1:] if x < λζφ[0]])
        χψβ = ϧΨΣ([x for x in λζφ[1:] if x >= λζφ[0]])
        return ντμ + [λζφ[0]] + χψβ

    def ɅξΦ(η: int) -> int:
        def μδε(ςτ: int) -> int:
            if ςτ == 0:
                return 0
            return (ςτ % 2) + μδε(ςτ // 2)
        return μδε(η)

    def λσΚ(πθ: List[int]) -> List[int]:
        if len(πθ) <= 1:
            return πθ
        mid = len(πθ) // 2
        σΔΞ = λσΚ(πθ[:mid])
        δΛΨ = λσΚ(πθ[mid:])
        return MERGE(σΔΞ, δΛΨ)

    def MERGE(μνρ: List[int], ζχπ: List[int]) -> List[int]:
        if not μνρ:
            return ζχπ
        if not ζχπ:
            return μνρ
        if μνρ[0] < ζχπ[0]:
            return [μνρ[0]] + MERGE(μνρ[1:], ζχπ)
        else:
            return [ζχπ[0]] + MERGE(μνρ, ζχπ[1:])

    def ᾹβΓ(πθ: List[int]) -> List[int]:
        if not πθ:
            return πθ
        αΘΛ = ᾹβΓ(πθ[1:])
        ϭζ = πθ[0]
        τσ = 0
        while τσ < len(αΘΛ) and (ɅξΦ(αΘΛ[τσ]) < ɅξΦ(ϭζ) or
                                (ɅξΦ(αΘΛ[τσ]) == ɅξΦ(ϭζ) and αΘΛ[τσ] < ϭζ)):
            τσ += 1
        return αΘΛ[:τσ] + [ϭζ] + αΘΛ[τσ:]

    ρϝκ = ϧΨΣ(array_of_integers)
    υχφ = ᾹβΓ(ρϝκ)
    return υχφ