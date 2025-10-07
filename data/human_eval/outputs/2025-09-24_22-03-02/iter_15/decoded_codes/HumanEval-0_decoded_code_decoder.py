from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    for idx in range(len(numbers)):
        elem = numbers[idx]
        for idx2 in range(len(numbers)):
            elem2 = numbers[idx2]
            if idx != idx2:
                distance = abs(elem - elem2)
                if distance < threshold:
                    return True
    return False