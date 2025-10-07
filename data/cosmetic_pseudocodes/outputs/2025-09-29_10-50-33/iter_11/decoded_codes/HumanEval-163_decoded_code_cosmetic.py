from typing import List


def generate_integers(param_x: int, param_y: int) -> List[int]:
    start_limit: int = 2 if 2 > (param_x if param_x < param_y else param_y) else (param_x if param_x < param_y else param_y)
    end_limit: int = 8 if 8 < (param_x if param_x > param_y else param_y) else (param_x if param_x > param_y else param_y)
    result_seq: List[int] = []
    index: int = start_limit
    while index <= end_limit:
        if index % 2 == 0:
            result_seq.append(index)
        index += 1
    return result_seq