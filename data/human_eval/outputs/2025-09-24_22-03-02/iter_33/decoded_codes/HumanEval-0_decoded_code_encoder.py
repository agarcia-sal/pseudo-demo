from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    length = len(numbers)
    for idx in range(length):
        elem = numbers[idx]
        for idx2 in range(length):
            if idx != idx2:
                difference = elem - numbers[idx2]
                distance = abs(difference)
                if distance < threshold:
                    return True
    return False