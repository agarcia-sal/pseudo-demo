from typing import List

def has_close_elements(list_of_numbers: List[float], threshold_value: float) -> bool:
    outer_position: int = 0
    length: int = len(list_of_numbers)
    while outer_position < length:
        first_value: float = list_of_numbers[outer_position]
        inner_position: int = 0
        while inner_position < length:
            if inner_position != outer_position:
                gap: float = first_value - list_of_numbers[inner_position]
                if gap < 0:
                    gap = -gap
                if gap < threshold_value:
                    return True
            inner_position += 1
        outer_position += 1
    return False