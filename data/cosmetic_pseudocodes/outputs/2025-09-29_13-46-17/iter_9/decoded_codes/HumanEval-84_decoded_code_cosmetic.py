from typing import Callable


def solve(integer_N: int) -> str:
    def ξΛκ(ζΩ: int) -> int:
        if ζΩ == 0:
            return 0
        return ξΛκ(ζΩ // 10) + (ζΩ % 10)

    def 𝛱ψ(θ: int) -> str:
        def βδ(λμ: str, νξ: int) -> str:
            if νξ == 0:
                return λμ
            return βδ(λμ + str(νξ % 2), νξ // 2)

        return βδ("", θ)

    ѰϬ: int = ξΛκ(integer_N)
    ργ: str = 𝛱ψ(ѰϬ)
    ΙШΨ: str = ""
    λϙ: int = 2
    while λϙ < len(ργ):
        ΙШΨ += ργ[λϙ]
        λϙ += 1
    return ΙШΨ