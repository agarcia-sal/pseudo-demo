from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Checks if there exist two distinct elements in 'numbers'
    whose absolute difference is less than 'threshold'.
    """
    n = len(numbers)
    # Iterate through all pairs without repeating pairs
    for i in range(n):
        for j in range(i + 1, n):
            if abs(numbers[i] - numbers[j]) < threshold:
                return True
    return False