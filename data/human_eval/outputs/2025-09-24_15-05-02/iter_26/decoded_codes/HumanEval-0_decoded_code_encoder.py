from typing import List

def has_close_elements(list_of_numbers: List[float], threshold: float) -> bool:
    length = len(list_of_numbers)
    if length < 2:
        return False
    for idx, elem in enumerate(list_of_numbers):
        for idx2, elem2 in enumerate(list_of_numbers):
            if idx != idx2:
                if abs(elem - elem2) < threshold:
                    return True
    return False