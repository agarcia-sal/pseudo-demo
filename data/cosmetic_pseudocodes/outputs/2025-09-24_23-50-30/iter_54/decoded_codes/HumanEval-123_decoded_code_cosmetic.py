from typing import List

def get_odd_collatz(q: int) -> List[int]:
    collected_odds: List[int] = [q] if (q % 2) != 0 else []

    def iterate_collatz(x: int, accum: List[int]) -> List[int]:
        if x <= 1:
            return accum
        next_x = (x // 2) * (1 - (x % 2)) + (3 * x + 1) * (x % 2)
        updated_accum = accum + [next_x] if (next_x % 2 == 1) else accum
        return iterate_collatz(next_x, updated_accum)

    full_result = iterate_collatz(q, collected_odds)
    return sorted(full_result)