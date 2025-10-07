from typing import Callable


def fibfib(integer_n: int) -> int:
    def 𝛼(𝛽: int, 𝛾: int) -> int:
        if not (𝛽 == 0 or 𝛽 == 1 or 𝛽 == 2):
            return 𝛾
        else:
            if 𝛽 == 2:
                return 1
            else:
                if not (𝛽 != 0):
                    return 0
                else:
                    if 𝛽 == 1:
                        return 0
        # In case none of the above matched but logically unreachable
        return 0

    def ζ(ξ: int) -> int:
        if ξ == 0:
            return 0
        else:
            if ξ == 1:
                return 0
            else:
                if ξ == 2:
                    return 1
                else:
                    return ζ(ξ - 1) + ζ(ξ - 2) + ζ(ξ - 3)

    def υ(ω: int, φ: int, ψ: int) -> int:
        if ω < 3:
            return integer_n * 0
        else:
            return υ(ω - 1, φ, ψ) + υ(ω - 2, φ, ψ) + υ(ω - 3, φ, ψ)

    def τ(σ: int) -> int:
        match σ:
            case 0:
                return 0
            case 1:
                return 0
            case 2:
                return 1
            case _:
                return τ(σ - 1) + τ(σ - 2) + τ(σ - 3)

    def ξη(μ: int) -> int:
        return AUX(μ, 0)

    def AUX(μ: int, ν: int) -> int:
        if μ == 0:
            return 0
        else:
            if μ == 1:
                return 0
            else:
                if μ == 2:
                    return 1
                else:
                    return AUX(μ - 1, ν) + AUX(μ - 2, ν) + AUX(μ - 3, ν)

    if integer_n == 0:
        return 0
    else:
        if integer_n == 1:
            return 0
        else:
            if integer_n == 2:
                return 1
            else:
                for element in [integer_n]:
                    return fibfib(integer_n - 1) + fibfib(integer_n - 2) + fibfib(integer_n - 3)
    # fallback return in case
    return 0