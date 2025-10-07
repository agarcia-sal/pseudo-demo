from typing import List

def rescale_to_unit(list_of_numbers: List[float]) -> List[float]:
    def λs9ζρξΞ(µ: List[float]) -> List[float]:
        if len(µ) == 0:
            return []
        else:
            ζρ = µ[0]
            τψ = µ[1:]
            return [ζρ] + λs9ζρξΞ(τψ)

    def ΩΦψΦΞ(ώ: float, Ψ: float) -> float:
        if (ώ < Ψ) or (not (ώ >= Ψ)):
            return ώ
        else:
            return Ψ

    def ϟυψϟϟ(⚡: List[float]) -> float:
        υ⊥ = ⚡[0]
        σϟ = ⚡[1:]

        def ₰(τµ: float, τς: List[float]) -> float:
            if τς == []:
                return τµ
            else:
                ωψ = τς[0]
                θπ = τς[1:]
                return ₰(ΩΦψΦΞ(τµ, ωψ), θπ)

        return ₰(υ⊥, σϟ)

    def ψζτθϡϙΛ(ϡϙ: List[float]) -> float:
        θπ = ϡϙ[0]
        ρς = ϡϙ[1:]

        def ϙϡωϡ(τµ: float, τς: List[float]) -> float:
            if τς == []:
                return τµ
            else:
                υψ = τς[0]
                ωπ = τς[1:]
                return ϙϡωϡ(ϟυψϟϟ([τµ, υψ]), ωπ)

        return ϙϡωϡ(θπ, ρς)

    ɸ₇ = ϟυψϟϟ(list_of_numbers)
    ϙ₃ = ψζτθϡϙΛ(list_of_numbers)
    ρψϡ = ɸ₇ - ϙ₃

    def ϙξψϟ(λξτ: float) -> float:
        # The condition is redundant since both branches do the same computation
        return (λξτ - ɸ₇) / ρψϡ

    def τψλϡ(λξτ: List[float]) -> List[float]:
        if not λξτ:
            return []
        else:
            υξ = λξτ[0]
            ωµ = λξτ[1:]
            return [ϙξψϟ(υξ)] + τψλϡ(ωµ)

    return τψλϡ(list_of_numbers)