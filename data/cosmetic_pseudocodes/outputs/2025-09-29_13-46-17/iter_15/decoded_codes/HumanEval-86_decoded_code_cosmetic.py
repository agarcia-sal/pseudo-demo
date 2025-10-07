from typing import List


def anti_shuffle(input_string: str) -> str:
    def νξλχ(ャ: List[str]) -> List[str]:
        if len(ャ) <= 1:
            return [ャ[0]]  # single element list
        return νξλχ(ャ[1:]) + [ャ[0]]

    def 𝛉𝛂𝛔𝛕(𐌀: List[str]) -> List[str]:
        if not 𐌀:
            return []
        if len(𐌀) <= 1:
            return 𐌀
        𝛍 = νξλχ(𐌀)[0]  # reversed first element
        ϕ = [c for c in 𐌀 if c < 𝛍]
        ψ = [c for c in 𐌀 if c == 𝛍]
        ω = [c for c in 𐌀 if c > 𝛍]
        return 𝛉𝛂𝛔𝛕(ϕ) + ψ + 𝛉𝛂𝛔𝛕(ω)

    def µϙρστ(χτζ: List[str]) -> str:
        if not χτζ:
            return ""
        if len(χτζ) == 1:
            return χτζ[0]
        return χτζ[0] + µϙρστ(χτζ[1:])

    def επφλ(υω: str) -> List[str]:
        def ztw(ξφζ: List[str], κρσ: int) -> List[str]:
            if κρσ >= len(ξφζ):
                return []
            β = ξφζ[κρσ]
            α = 𝛉𝛂𝛔𝛕(list(β))
            χα = µϙρστ(α)
            return [χα] + ztw(ξφζ, κρσ + 1)
        ωξζ = υω.split(" ")
        return ztw(ωξζ, 0)

    ψλπρ = επφλ(input_string)
    σπϙ = ""

    def λσξλ(ξλζ: List[str], ιπθ: int, κσρ: str) -> str:
        if ιπθ >= len(ξλζ):
            return κσρ
        if κσρ == "":
            return λσξλ(ξλζ, ιπθ + 1, ξλζ[ιπθ])
        return λσξλ(ξλζ, ιπθ + 1, κσρ + " " + ξλζ[ιπθ])

    ϱω = λσξλ(ψλπρ, 0, σπϙ)
    return ϱω