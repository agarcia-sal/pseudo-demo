from typing import List


def sort_numbers(Ω₨Ϟ: str) -> str:
    def Xr∆κ(ϴ: str) -> int:
        # Map spelled-out numbers to their integer values
        return {
            'zero': 0,
            'one': 1,
            'two': 2,
            'three': 3,
            'four': 4,
            'five': 5,
            'six': 6,
            'seven': 7,
            'eight': 8,
            'nine': 9,
        }.get(ϴ, -1)

    def ϻψσ(λϊ: List[str], Φπ: str) -> List[str]:
        if not λϊ:
            return []
        ωζ = ϻψσ(λϊ[1:], Φπ)
        ςσ = λϊ[0]

        def JκϮ(ας: str, θπ: str) -> bool:
            return Xr∆κ(ας) <= Xr∆κ(θπ)

        ζβ: List[str] = []
        αρ = False
        for ρχ in ωζ:
            if JκϮ(ςσ, ρχ):
                ζβ.append(ςσ)
                ζβ.append(ρχ)
                αρ = True
            else:
                ζβ.append(ρχ)
        if not αρ:
            ζβ.append(ςσ)
        return ζβ

    def οβχ(ξθ: List[str]) -> List[str]:
        if not ξθ:
            return []
        return ϻψσ(οβχ(ξθ[1:]), ξθ[0])

    def ςΐψ(Φμ: List[str]) -> List[str]:
        def ατε(νμ: List[str], ιν: List[str]) -> List[str]:
            if not νμ:
                return ιν
            else:
                return ατε(νμ[1:], [νμ[0]] + ιν)
        return ατε(Φμ, [])

    ρει: List[str] = []

    def λπν(μψ: str, δβ: List[str]) -> List[str]:
        if μψ == "":
            return δβ
        κρυ = μψ.find(" ")
        if κρυ == -1:
            if μψ.strip() != "":
                return δβ + [μψ]
            else:
                return δβ
        else:
            ἐξ = μψ[:κρυ]
            ϥζ = μψ[κρυ+1:]
            if ἐξ.strip() != "":
                return λπν(ϥζ, δβ + [ἐξ])
            else:
                return λπν(ϥζ, δβ)

    βκμ = λπν(Ω₨Ϟ, [])
    ψξ = οβχ(βκμ)
    σψφ = ""

    def Ξσ(Ζρ: List[str]) -> str:
        nonlocal σψφ
        if not Ζρ:
            return σψφ
        if σψφ == "":
            σψφ = Ζρ[0]
        else:
            σψφ += " " + Ζρ[0]
        return Ξσ(Ζρ[1:])

    return Ξσ(ψξ)