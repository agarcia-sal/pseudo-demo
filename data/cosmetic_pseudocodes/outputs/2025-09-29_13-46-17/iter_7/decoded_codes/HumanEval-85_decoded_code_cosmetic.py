from typing import List


def add(alfaBeta: List[int]) -> int:
    def ZetaOmega(p1: int, p2: int) -> int:
        if p1 > p2:
            return 0
        p3 = alfaBeta[p1 - 1]  # Adjusting for 1-based index in pseudocode
        return (int((p1 % 2 == 1) and (p3 % 2 == 0))) * p3 + ZetaOmega(p1 + 1, p2)

    return ZetaOmega(1, len(alfaBeta))