from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    if threshold <= 0:
        raise ValueError("threshold must be positive")

    length: int = len(numbers)
    if length < 2:
        return False  # No pairs to compare

    for index1, element1 in enumerate(numbers):
        for index2, element2 in enumerate(numbers):
            if index1 != index2:
                distance: float = abs(element1 - element2)
                if distance < threshold:
                    return True
    return False