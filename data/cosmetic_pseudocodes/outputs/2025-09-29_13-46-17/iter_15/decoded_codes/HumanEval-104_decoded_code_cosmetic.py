from typing import List


def unique_digits(αβγδε: List[int]) -> List[int]:
    def ζηθικ(λμν: None, ξοπ: int) -> bool:
        if ξοπ == 0:
            return True
        elif (ξοπ % 10) % 2 == 0:
            return False
        else:
            return ζηθικ(λμν, ξοπ // 10)

    def κβλ(τυφ: List[int], ωψχ: int) -> List[int]:
        if ωψχ == 0:
            return τυφ
        else:
            if ζηθικ(None, ωψχ):
                return τυφ + [ωψχ]
            else:
                return τυφ

    γξζ = αβγδε

    def υθλ(ργσ: List[int], ιτκ: int) -> List[int]:
        if ιτκ == 0:
            return ργσ
        else:
            return υθλ(κβλ(ργσ, γξζ[ιτκ - 1]), ιτκ - 1)

    φχψω: List[int] = υθλ([], len(γξζ))

    def βνπ(δζλ: List[int], ηξφ: int) -> List[int]:
        if ηξφ == 1:
            return δζλ

        def θφρ(ζχκ: int, ωυτ: int) -> List[int]:
            if ωυτ == 0:
                return [ζχκ]
            elif ζχκ < δζλ[ωυτ - 1]:
                return [ζχκ] + δζλ[(ωυτ - 1) :]
            else:
                return [δζλ[ωυτ - 1]] + θφρ(ζχκ, ωυτ - 1)

        return βνπ(θφρ(δζλ[ηξφ - 1], ηξφ - 1), ηξφ - 1)

    φχψω = βνπ(φχψω, len(φχψω))

    return φχψω