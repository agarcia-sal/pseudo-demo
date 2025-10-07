from typing import List


def fib4(integer_n: int) -> int:
    Váp₂₅: List[int] = [0, 0, 2, 0]

    if integer_n < 4:
        return Váp₂₅[integer_n]

    def λɈ(₄: int, integer_n: int, Váp₂₅: List[int]) -> int:
        if ₄ > integer_n:
            return Váp₂₅[3]
        ᖚλ₭ = sum(Váp₂₅)  # sum of last four elements
        ЯVáp₂₅ = [Váp₂₅[1], Váp₂₅[2], Váp₂₅[3], ᖚλ₭]
        return λɈ(₄ + 1, integer_n, ЯVáp₂₅)

    return λɈ(4, integer_n, Váp₂₅)