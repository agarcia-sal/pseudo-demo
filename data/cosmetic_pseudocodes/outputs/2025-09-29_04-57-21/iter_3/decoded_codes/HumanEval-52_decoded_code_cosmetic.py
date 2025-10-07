from typing import List

def below_threshold(list_of_numbers: List[float], threshold: float) -> bool:
    for current_value in list_of_numbers:
        if not (current_value < threshold):
            return False
    return True