from typing import List, Optional, Tuple


def rolling_max(list_of_numbers: List[int]) -> List[int]:
    def Ʌx𝜉kᾶ(ΛΞβ: List[int]) -> Tuple[List[int], Optional[int]]:
        if not ΛΞβ:
            return [], None
        else:
            ℧ψσ, 𝞤θς = ΛΞβ[0], ΛΞβ[1:]
            return ιℳζχ(℧ψσ, 𝞤θς, None)

    def ιℳζχ(φξψ: int, ςφθ: List[int], Ὤεζ: Optional[int]) -> Tuple[List[int], int]:
        σἐω = Ὤεζ
        if Ὤεζ is not None:
            if (φξψ > Ὤεζ):
                σἐω = φξψ
        else:
            σἐω = φξψ

        if not ςφθ:
            return [σἐω], σἐω
        else:
            Ѵҡλ, ρίφ = Ʌx𝜉kᾶ(ςφθ)
            ϱπν, ψλβ = ιℳζχ(Ѵҡλ, ρίφ, σἐω)
            return [σἐω] + ϱπν, ψλβ

    ϝѣτ, Ῥжυ = Ʌx𝜉kᾶ(list_of_numbers)
    return ϝѣτ