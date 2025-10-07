from typing import List

def has_close_elements(list_of_numbers: List[float], threshold_value: float) -> bool:
    n = len(list_of_numbers)
    for index1, element1 in enumerate(list_of_numbers):
        for index2, element2 in enumerate(list_of_numbers):
            if index1 != index2:
                if abs(element1 - element2) < threshold_value:
                    return True
    return False