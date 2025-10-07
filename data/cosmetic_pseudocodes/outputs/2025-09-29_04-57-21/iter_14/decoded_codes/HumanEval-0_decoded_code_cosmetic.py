from typing import List


def has_close_elements(list_of_numbers: List[float], threshold_value: float) -> bool:
    outer_pos: int = 0
    length: int = len(list_of_numbers)
    while outer_pos < length:
        outer_elem: float = list_of_numbers[outer_pos]
        inner_pos: int = 0
        while inner_pos < length:
            if outer_pos == inner_pos:
                inner_pos += 1
                continue
            inner_elem: float = list_of_numbers[inner_pos]
            gap: float = outer_elem - inner_elem
            abs_gap: float = gap if gap >= 0 else -gap
            if abs_gap < threshold_value:
                return True
            inner_pos += 1
        outer_pos += 1
    return False