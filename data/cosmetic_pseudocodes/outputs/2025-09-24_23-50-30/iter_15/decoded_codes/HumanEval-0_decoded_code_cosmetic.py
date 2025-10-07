from typing import List


def has_close_elements(list_of_numbers: List[float], threshold_value: float) -> bool:
    pointer_a: int = 0
    length: int = len(list_of_numbers)
    while pointer_a < length:
        pointer_b: int = 0
        while pointer_b < length:
            if pointer_a != pointer_b:
                diff_measure: float = list_of_numbers[pointer_a] - list_of_numbers[pointer_b]
                if diff_measure < 0:
                    diff_measure = -diff_measure
                if diff_measure < threshold_value:
                    return True
            pointer_b += 1
        pointer_a += 1
    return False