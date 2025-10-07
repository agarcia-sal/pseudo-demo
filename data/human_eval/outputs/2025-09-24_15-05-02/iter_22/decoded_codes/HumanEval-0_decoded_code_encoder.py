from typing import List

def has_close_elements(list_of_numbers: List[float], threshold_value: float) -> bool:
    length = len(list_of_numbers)
    for index_one in range(length):
        element_one = list_of_numbers[index_one]
        for index_two in range(length):
            if index_one != index_two:
                element_two = list_of_numbers[index_two]
                distance_to_compare = abs(element_one - element_two)
                if distance_to_compare < threshold_value:
                    return True
    return False