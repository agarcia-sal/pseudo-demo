from typing import List

def has_close_elements(numbers: List[int], threshold: int) -> bool:
    length = len(numbers)
    for idx in range(length):
        elem = numbers[idx]
        for idx2 in range(length):
            elem2 = numbers[idx2]
            if idx != idx2:
                if abs(elem - elem2) < threshold:
                    return True
    return False