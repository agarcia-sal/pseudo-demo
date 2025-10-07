from typing import List


def has_close_elements(list_of_numbers: List[float], threshold_value: float) -> bool:
    position_a: int = 0
    length: int = len(list_of_numbers)
    while position_a < length:
        position_b: int = 0
        while position_b < length:
            if position_a == position_b:
                position_b += 1
                continue
            value_diff: float = abs(list_of_numbers[position_a] - list_of_numbers[position_b])
            if threshold_value <= value_diff:
                position_b += 1
                continue
            return True
        position_a += 1
    return False