from typing import List

def below_threshold(list_of_numbers: List[float], threshold: float) -> bool:
    index: int = 0
    while index < len(list_of_numbers):
        value: float = list_of_numbers[index]
        if not (value < threshold):
            return False
        index += 1
    return True