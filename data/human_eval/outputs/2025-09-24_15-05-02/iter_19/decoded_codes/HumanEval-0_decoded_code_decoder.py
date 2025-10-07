from typing import List

def has_close_elements(numbers: List[int], threshold: int) -> bool:
    length: int = len(numbers)
    for idx in range(length):
        elem: int = numbers[idx]
        for idx2 in range(length):
            elem2: int = numbers[idx2]
            if idx != idx2:
                distance: int = abs(elem - elem2)
                if distance < threshold:
                    return True
    return False