from typing import List

def get_odd_collatz(n: int) -> List[int]:
    def append_odd_numbers(value: int, accumulation: List[int]) -> List[int]:
        if value <= 1:
            return accumulation

        if value % 2 == 0:
            next_val = value // 2
        else:
            next_val = value * 3 + 1

        if next_val % 2 != 0:
            new_accumulation = accumulation + [next_val]
        else:
            new_accumulation = accumulation

        return append_odd_numbers(next_val, new_accumulation)

    initial_list: List[int] = [n] if n % 2 != 0 else []
    collected_odds = append_odd_numbers(n, initial_list)
    return sorted(collected_odds)