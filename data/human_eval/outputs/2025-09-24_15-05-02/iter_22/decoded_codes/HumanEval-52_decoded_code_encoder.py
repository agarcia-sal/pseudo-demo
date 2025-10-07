from typing import List


def below_threshold(list_of_numbers: List[float], threshold: float) -> bool:
    for element in list_of_numbers:
        if element >= threshold:
            return False
    return True