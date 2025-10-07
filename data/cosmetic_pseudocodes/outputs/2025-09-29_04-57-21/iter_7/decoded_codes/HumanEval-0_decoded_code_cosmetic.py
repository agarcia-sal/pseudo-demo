from typing import List


def has_close_elements(list_of_numbers: List[float], threshold_value: float) -> bool:
    outer_index: int = 0
    length: int = len(list_of_numbers)
    while outer_index < length:
        first_element: float = list_of_numbers[outer_index]
        inner_index: int = 0
        while inner_index < length:
            if outer_index != inner_index:
                delta: float = first_element - list_of_numbers[inner_index]
                if delta < 0:
                    delta = -delta
                if delta < threshold_value:
                    return True
            inner_index += 1
        outer_index += 1
    return False