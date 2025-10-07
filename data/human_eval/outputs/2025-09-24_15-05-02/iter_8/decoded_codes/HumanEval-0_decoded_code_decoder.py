from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    length: int = len(numbers)
    for idx in range(length):
        elem: float = numbers[idx]
        for idx2 in range(length):
            if idx != idx2:
                elem2: float = numbers[idx2]
                distance: float = abs(elem - elem2)
                if distance < threshold:
                    return True
    return False