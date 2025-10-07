from typing import List

def has_close_elements(list_of_numbers: List[float], threshold: float) -> bool:
    length = len(list_of_numbers)
    for index1 in range(length):
        element1 = list_of_numbers[index1]
        for index2 in range(index1 + 1, length):
            element2 = list_of_numbers[index2]
            if abs(element1 - element2) < threshold:
                return True
    return False