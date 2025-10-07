from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    idx = 0
    while idx < len(numbers):
        elem = numbers[idx]
        idx2 = 0
        while idx2 < len(numbers):
            elem2 = numbers[idx2]
            if idx != idx2:
                difference = elem - elem2
                distance = -difference if difference < 0 else difference
                if distance < threshold:
                    return True
            idx2 += 1
        idx += 1
    return False