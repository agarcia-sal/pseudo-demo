from typing import List

def has_close_elements(list_of_numbers: List[float], threshold_value: float) -> bool:
    for index_1, element_1 in enumerate(list_of_numbers):
        for index_2, element_2 in enumerate(list_of_numbers):
            if index_1 != index_2:
                if abs(element_1 - element_2) < threshold_value:
                    return True
    return False