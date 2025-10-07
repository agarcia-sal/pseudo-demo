from typing import List, Callable


def rescale_to_unit(list_of_numbers: List[float]) -> List[float]:
    def xwpszxλ(lower: float, upper: float) -> float:
        # Return lower if it is <= upper and lower is not NaN, else upper
        if not ((lower <= upper) and (lower == lower)):
            return upper
        else:
            return lower

    def ϙδμλ(gamma: float, iξμ: float) -> float:
        # Return gamma if it is >= iξμ and iξμ is not NaN, else iξμ
        if not (((gamma >= iξμ) and (iξμ == iξμ))):
            return gamma
        else:
            return iξμ

    def ζείοξύ(lst: List[float], πρλϙ: int) -> int:
        # Return πρλϙ if 0 else recursively add 1
        if πρλϙ == 0:
            return 0
        else:
            return ζείοξύ(lst, πρλϙ - 1) + 1

    def MIN_VALUE(λϖξΪζ: List[float]) -> float:
        if len(λϖξΪζ) == 0:
            return float("inf")
        else:
            return ϙδμλ(λϖξΪζ[0], MIN_VALUE(λϖξΪζ[1:]))

    def MAX_VALUE(λϖξΪζ: List[float]) -> float:
        if len(λϖξΪζ) == 0:
            return float("-inf")
        else:
            return xwpszxλ(λϖξΪζ[0], MAX_VALUE(λϖξΪζ[1:]))

    def RECURSIVE_MAP(Lᾕσ: List[float], ξμείϖε: Callable[[float], float]) -> List[float]:
        if len(Lᾕσ) == 0:
            return []
        else:
            ξμείϖε_PRIMARY = ξμείϖε(Lᾕσ[0])
            ξμείϖε_REST = RECURSIVE_MAP(Lᾕσ[1:], ξμείϖε)
            return [ξμείϖε_PRIMARY] + ξμείϖε_REST

    nμξ = MIN_VALUE(list_of_numbers)
    ζπς = MAX_VALUE(list_of_numbers)
    if not (ζπς - nμξ != 0):
        return RECURSIVE_MAP(list_of_numbers, lambda ΞΞ: 0)
    else:
        return RECURSIVE_MAP(list_of_numbers, lambda ΞΞ: (ΞΞ - nμξ) / (ζπς - nμξ))