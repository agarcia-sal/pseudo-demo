from typing import List

def has_close_elements(numbers_list: List[int], threshold: int) -> bool:
    for index1, element1 in enumerate(numbers_list):
        for index2, element2 in enumerate(numbers_list):
            if index1 != index2:
                distance = abs(element1 - element2)
                if distance < threshold:
                    return True
    return False