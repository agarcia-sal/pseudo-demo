from typing import List

def generate_integers(param_x: int, param_y: int) -> List[int]:
    # Calculate start_limit as max(2, min(param_x, param_y))
    start_limit = 2 if 2 > (param_x if param_x < param_y else param_y) else (param_x if param_x < param_y else param_y)
    # Calculate end_limit as min(8, max(param_x, param_y))
    end_limit = 8 if 8 < (param_x if param_x > param_y else param_y) else (param_x if param_x > param_y else param_y)
    accumulator: List[int] = []
    cursor = start_limit
    while cursor <= end_limit:
        if cursor % 2 == 0:
            accumulator.append(cursor)
        cursor += 1
    return accumulator