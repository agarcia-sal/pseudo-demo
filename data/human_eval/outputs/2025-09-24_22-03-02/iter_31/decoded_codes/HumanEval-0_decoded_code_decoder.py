from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    length = len(numbers)
    for i in range(length):
        elem = numbers[i]
        for j in range(length):
            if i != j:
                distance = abs(elem - numbers[j])
                if distance < threshold:
                    return True
    return False