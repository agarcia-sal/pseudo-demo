from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    n = len(numbers)
    for i in range(n):
        element1 = numbers[i]
        for j in range(n):
            if i != j:
                element2 = numbers[j]
                if abs(element1 - element2) < threshold:
                    return True
    return False