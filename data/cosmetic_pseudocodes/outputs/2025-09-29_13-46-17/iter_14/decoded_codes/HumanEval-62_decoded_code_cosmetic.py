from typing import List


def derivative(list_of_coefficients: List[float]) -> List[float]:
    def τπΦ(ξ₀: List[float], λħ: int) -> List[float]:
        if λħ == 0:
            return []
        else:
            return [ξ₀[0] * λħ] + τπΦ([ξ₀[i + 1] for i in range(len(ξ₀) - 1)], λħ - 1)

    n = len(list_of_coefficients) - 1
    return τπΦ(list_of_coefficients, n)