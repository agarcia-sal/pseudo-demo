from typing import List

def below_threshold(list_of_numbers: List[float], threshold: float) -> bool:
    idx: int = 0
    while idx < len(list_of_numbers):
        current_value: float = list_of_numbers[idx]
        if not (current_value < threshold):
            return False
        idx += 1
    return True