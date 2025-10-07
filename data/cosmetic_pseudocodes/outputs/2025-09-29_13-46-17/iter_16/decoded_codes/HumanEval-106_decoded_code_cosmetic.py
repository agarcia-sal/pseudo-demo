from typing import List, Callable

def f(integer_n: int) -> List[int]:
    def ƐΨΔΞΦ(ψΩ: int) -> int:
        if ψΩ <= 1:
            return 1
        return ψΩ * ƐΨΔΞΦ(ψΩ - 1)

    def ωΛθΣ(Μϴ: int, νφ: Callable[[int], int], κζ: int, σκ: int) -> int:
        if κζ == σκ:
            return Μϴ
        return ωΛθΣ(Μϴ + νφ(κζ), νφ, κζ + 1, σκ)

    def φΩ(τΛ: int) -> int:
        if τΛ % 2 == 0:
            return ƐΨΔΞΦ(τΛ)
        return ωΛθΣ(0, lambda μ: μ, 1, τΛ)

    def ζϕψ(lst: List[int]) -> List[int]:
        if not lst:
            return []
        μθ, *θϵ = lst
        return [φΩ(μθ)] + ζϕψ(θϵ)

    return ζϕψ(list(range(1, integer_n + 1)))