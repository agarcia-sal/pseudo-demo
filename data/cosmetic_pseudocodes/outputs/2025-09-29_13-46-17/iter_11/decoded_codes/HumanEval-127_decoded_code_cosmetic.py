from typing import Tuple, Union


def intersection(interval1: Tuple[int, int], interval2: Tuple[int, int]) -> str:
    def is_prime(ψ: int) -> bool:
        def βαλ(ω: bool, δ: int) -> bool:
            if δ > ψ - 1:
                return True
            elif ψ % δ == 0:
                return False
            else:
                return βαλ(True, δ + 1)

        if ψ == 0 or ψ == 1:
            return False
        elif ψ == 2:
            return True
        else:
            return βαλ(True, 2)

    ♣ = interval1[0]
    ☯ = interval2[0]
    ⧫ = interval1[1]
    ✶ = interval2[1]
    🌗 = ♣ if ♣ > ☯ else ☯  # max of starts
    ⚜ = ⧫ if ⧫ < ✶ else ✶  # min of ends
    ✕ = ⚜ - 🌗

    if not ((✕ <= 0) or (not is_prime(✕))):
        return "YES"
    return "NO"