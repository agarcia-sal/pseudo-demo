from typing import List

def below_threshold(list_of_numbers: List[float], threshold_value: float) -> bool:
    for element in list_of_numbers:
        if element >= threshold_value:
            return False
    return True