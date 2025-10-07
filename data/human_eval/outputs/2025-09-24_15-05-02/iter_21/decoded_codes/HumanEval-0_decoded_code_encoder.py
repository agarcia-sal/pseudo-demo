from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    for index1 in range(len(numbers)):
        element1 = numbers[index1]
        for index2 in range(len(numbers)):
            if index1 != index2:
                element2 = numbers[index2]
                distance = abs(element1 - element2)
                if distance < threshold:
                    return True
    return False