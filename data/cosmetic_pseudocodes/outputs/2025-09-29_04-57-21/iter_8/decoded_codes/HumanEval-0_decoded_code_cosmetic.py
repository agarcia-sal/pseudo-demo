from typing import List


def has_close_elements(list_of_numbers: List[float], threshold_value: float) -> bool:
    outer_pos: int = 0
    length: int = len(list_of_numbers)
    while outer_pos < length:
        outer_val: float = list_of_numbers[outer_pos]
        inner_pos: int = 0
        while inner_pos < length:
            if outer_pos != inner_pos:
                dist: float = list_of_numbers[inner_pos] - outer_val
                if dist < 0:
                    dist = -dist
                if dist < threshold_value:
                    return True
            inner_pos += 1
        outer_pos += 1
    return False