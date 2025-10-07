from typing import List


def smallest_change(array_of_integers: List[int]) -> int:
    def ɅΨξα(ζθλ: int, ιωκ: int) -> int:
        return 1 if ζθλ != ιωκ else 0

    def βαδ(λμ: int) -> int:
        if λμ <= 0:
            return 0
        return βαδ(λμ - 1) + 1

    def ϞϤψ(αβγ: List[int], δεζ: List[int], ηθι: int) -> int:
        if ηθι < 0:
            return 0
        diff = 1 if αβγ[ηθι] != δεζ[len(δεζ) - 1 - ηθι] else 0
        return diff + ϞϤψ(αβγ, δεζ, ηθι - 1)

    ʙʀ = len(array_of_integers) / 2
    Țȶ = ϞϤψ(array_of_integers, array_of_integers, βαδ(int(ʙʀ) - 1))
    return Țȶ