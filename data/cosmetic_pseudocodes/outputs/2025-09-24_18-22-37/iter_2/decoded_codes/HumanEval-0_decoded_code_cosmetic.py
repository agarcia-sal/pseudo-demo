from typing import List


def has_close_elements(list_of_numbers: List[float], threshold_value: float) -> bool:
    current_pos: int = 0
    length: int = len(list_of_numbers)
    while current_pos < length:
        other_pos: int = 0
        while other_pos < length:
            if current_pos != other_pos:
                delta: float = list_of_numbers[current_pos] - list_of_numbers[other_pos]
                if delta < 0:
                    delta = -delta
                if delta < threshold_value:
                    return True
            other_pos += 1
        current_pos += 1
    return False