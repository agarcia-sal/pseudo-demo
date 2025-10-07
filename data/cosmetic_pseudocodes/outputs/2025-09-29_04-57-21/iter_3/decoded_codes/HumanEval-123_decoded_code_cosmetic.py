from typing import List


def get_odd_collatz(n: int) -> List[int]:
    if n % 2 != 1:
        collected_odds: List[int] = []
    else:
        collected_odds = [n]

    current_val = n

    while current_val > 1:
        if current_val % 2 == 0:
            current_val //= 2
        else:
            current_val = 3 * current_val + 1

        if current_val % 2 == 1:
            collected_odds.append(int(current_val))

    return sorted(collected_odds)