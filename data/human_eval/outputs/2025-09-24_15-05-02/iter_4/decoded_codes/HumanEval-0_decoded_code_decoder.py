from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    length = len(numbers)
    for index1 in range(length):
        element1 = numbers[index1]
        for index2 in range(length):
            if index1 != index2:
                element2 = numbers[index2]
                distance = abs(element1 - element2)
                if distance < threshold:
                    return True
    return False