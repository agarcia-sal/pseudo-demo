from typing import List


def has_close_elements(list_of_numbers: List[float], threshold_value: float) -> bool:
    outer_cursor: int = 0
    while outer_cursor < len(list_of_numbers):
        value_outer: float = list_of_numbers[outer_cursor]
        inner_cursor: int = 0
        while inner_cursor < len(list_of_numbers):
            if outer_cursor != inner_cursor:
                delta: float = value_outer - list_of_numbers[inner_cursor]
                if (delta < 0 and -delta < threshold_value) or (delta >= 0 and delta < threshold_value):
                    return True
            inner_cursor += 1
        outer_cursor += 1
    return False