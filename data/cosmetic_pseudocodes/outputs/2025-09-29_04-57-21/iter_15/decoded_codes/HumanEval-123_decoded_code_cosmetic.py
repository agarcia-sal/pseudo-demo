from typing import List


def get_odd_collatz(n: int) -> List[int]:
    odds_sequence: List[int] = [n] if n % 2 == 1 else []
    current_value: int = n

    while current_value > 1:
        if current_value % 2 == 0:
            current_value //= 2
        else:
            current_value = 3 * current_value + 1

        if current_value % 2 == 1:
            odds_sequence.append(current_value)

    return sorted(odds_sequence)