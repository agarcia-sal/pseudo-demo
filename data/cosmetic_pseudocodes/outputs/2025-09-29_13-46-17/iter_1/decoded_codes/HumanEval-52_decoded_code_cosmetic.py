from typing import List

def below_threshold(list_of_numbers: List[float], threshold: float) -> bool:
    for number in list_of_numbers:
        if number >= threshold:
            return False
    return True