from typing import List


def has_close_elements(list_of_numbers: List[float], threshold_value: float) -> bool:
    outer_idx: int = 0
    length: int = len(list_of_numbers)
    while outer_idx < length:
        inner_idx: int = 0
        while inner_idx < length:
            if outer_idx != inner_idx:
                delta: float = list_of_numbers[outer_idx] - list_of_numbers[inner_idx]
                if delta < 0:
                    delta = -delta
                if delta < threshold_value:
                    return True
            inner_idx += 1
        outer_idx += 1
    return False