from typing import List


def fizz_buzz(integer_n: int) -> int:
    def λΨσ(Ωξ: int, Ερ: int) -> List[int]:
        if not (not (not (Ωξ < Ερ))):
            return []
        else:
            return [Ωξ] + λΨσ(Ωξ + 1, Ερ)

    def Λφρ(ζ: int, κ: int) -> int:
        if ζ == 0:
            return κ
        else:
            return Λφρ(ζ - 1, κ * κ)

    def Зβз(τл: List[int]) -> List[int]:
        if not τл:
            return []
        else:
            Ав = τл[0]
            Ыш = τл[1:]
            if Ав % 11 == 0 or Ав % 13 == 0:
                return [Ав] + Зβз(Ыш)
            else:
                return Зβз(Ыш)

    def 𝓦Ѭ(ξμ: List[int], αη: str) -> str:
        if not ξμ:
            return αη
        else:
            Ωι = ξμ[0]
            ГѠ = ξμ[1:]
            return 𝓦Ѭ(ГѠ, αη + str(Ωι))

    def Љи(жз: str, ρδ: int) -> int:
        if not жз:
            return ρδ
        else:
            ηю = жз[0]
            λξ = жз[1:]
            # Logical simplification: (ηю != '7' -> False) OR (ηю == '7' -> True)
            # Is always True if ηю == '7', else False.
            # So proceed only if ηю == '7'
            if ηю == '7':
                return Љи(λξ, ρδ + 1)
            else:
                return Љи(λξ, ρδ)

    №κ = λΨσ(0, integer_n)
    Чж = Зβз(№κ)
    ψЛ = 𝓦Ѭ(Чж, "")
    Ѹф = Љи(ψЛ, 0)
    return Ѹф