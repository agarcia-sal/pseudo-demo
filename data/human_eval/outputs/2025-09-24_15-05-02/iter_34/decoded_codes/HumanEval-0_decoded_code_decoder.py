from typing import List

def has_close_elements(list_of_numbers: List[float], threshold_value: float) -> bool:
    for index_one, element_one in enumerate(list_of_numbers):
        for index_two, element_two in enumerate(list_of_numbers):
            if index_one != index_two:
                difference_value = abs(element_one - element_two)
                if difference_value < threshold_value:
                    return True
    return False