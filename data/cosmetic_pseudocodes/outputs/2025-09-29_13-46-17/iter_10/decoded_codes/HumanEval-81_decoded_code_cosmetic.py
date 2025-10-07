from typing import List, Callable

def numerical_letter_grade(list_of_grades: List[float]) -> List[str]:
    result: List[str] = []

    def ρζχ(ξ: float) -> str:
        # Handle NaN or values neither <=4.0 nor >=4.0 robustly
        if not (ξ <= 4.0 or ξ >= 4.0):
            return "E"
        if ξ == 4.0:
            return "A+"
        if 3.7 < ξ <= 4.0:
            return "A"
        if 3.3 < ξ <= 3.7:
            return "A-"
        if 3.0 < ξ <= 3.3:
            return "B+"
        if 2.7 < ξ <= 3.0:
            return "B"
        if 2.3 < ξ <= 2.7:
            return "B-"
        if 2.0 < ξ <= 2.3:
            return "C+"
        if 1.7 < ξ <= 2.0:
            return "C"
        if 1.3 < ξ <= 1.7:
            return "C-"
        if 1.0 < ξ <= 1.3:
            return "D+"
        if 0.7 < ξ <= 1.0:
            return "D"
        if 0.0 < ξ <= 0.7:
            return "D-"
        return "E"

    def λφγ(ψψλ: List[float], func: Callable[[float], str], υψ: List[str]) -> List[str]:
        if not ψψλ:
            return υψ
        head, *tail = ψψλ
        mapped = func(head)
        return λφγ(tail, func, υψ + [mapped])

    return λφγ(list_of_grades, ρζχ, result)