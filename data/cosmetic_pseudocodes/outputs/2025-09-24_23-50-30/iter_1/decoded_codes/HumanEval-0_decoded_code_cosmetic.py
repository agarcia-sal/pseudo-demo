from typing import List

def has_close_elements(list_of_numbers: List[float], threshold_value: float) -> bool:
    length_numbers: int = len(list_of_numbers)
    i: int = 0
    while i < length_numbers:
        j: int = 0
        while j < length_numbers:
            if i != j:
                diff: float = list_of_numbers[i] - list_of_numbers[j]
                if diff < 0:
                    diff = -diff
                if diff < threshold_value:
                    return True
            j += 1
        i += 1
    return False