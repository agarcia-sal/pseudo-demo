from typing import List

def has_close_elements(list_of_numbers: List[float], threshold: float) -> bool:
    length = len(list_of_numbers)
    for index1 in range(length):
        element1 = list_of_numbers[index1]
        for index2 in range(length):
            if index1 != index2:
                element2 = list_of_numbers[index2]
                distance = abs(element1 - element2)
                if distance < threshold:
                    return True
    return False