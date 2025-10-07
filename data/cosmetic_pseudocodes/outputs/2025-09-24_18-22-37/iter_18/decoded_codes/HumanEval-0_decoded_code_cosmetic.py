from typing import List


def has_close_elements(list_of_numbers: List[float], threshold_value: float) -> bool:
    iterator_a: int = 0
    while True:
        if iterator_a >= len(list_of_numbers):
            return False
        current_elem_a: float = list_of_numbers[iterator_a]
        iterator_b: int = 0
        while iterator_b < len(list_of_numbers):
            if iterator_a != iterator_b:
                temp_diff: float = current_elem_a - list_of_numbers[iterator_b]
                if temp_diff < 0:
                    temp_diff = -temp_diff
                if temp_diff < threshold_value:
                    return True
            iterator_b += 1
        iterator_a += 1