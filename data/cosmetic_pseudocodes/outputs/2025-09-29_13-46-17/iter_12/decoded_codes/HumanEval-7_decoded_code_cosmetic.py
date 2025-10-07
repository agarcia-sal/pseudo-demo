from typing import List


def filter_by_substring(αβγδεζηθικλμνξοπρσςτυφχψωабвгд: List[str], ыэюя: str) -> List[str]:
    ξυφχψωляльзелоте: List[str] = []
    κ = 0
    while κ < len(αβγδεζηθικλμνξοπρσςτυφχψωабвгд):
        μ = αβγδεζηθικλμνξοπρσςτυφχψωабвгд[κ]
        λ = 0
        ѵ = False
        while λ <= len(μ) - len(ыэюя):
            if len(ыэюя) + λ <= len(μ):
                if ыэюя == μ[λ : λ + len(ыэюя)]:
                    ѵ = True
                    break
            λ = λ + 1
        if ѵ:
            ξυφχψωляльзелоте.append(μ)
        κ = κ + 1
    return ξυφχψωляльзелоте