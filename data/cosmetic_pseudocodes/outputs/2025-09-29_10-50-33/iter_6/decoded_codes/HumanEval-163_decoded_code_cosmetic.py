from typing import List

def generate_integers(alpha: int, beta: int) -> List[int]:
    def collect_evens(current_value: int, ceiling: int, accumulator: List[int]) -> List[int]:
        if current_value > ceiling:
            return accumulator
        if current_value % 2 == 0:
            accumulator.append(current_value)
        return collect_evens(current_value + 1, ceiling, accumulator)

    min_limit = alpha if alpha < beta else beta
    max_limit = alpha if alpha > beta else beta
    floor_limit = max(2, min_limit)
    ceil_limit = min(8, max_limit)

    return collect_evens(floor_limit, ceil_limit, [])