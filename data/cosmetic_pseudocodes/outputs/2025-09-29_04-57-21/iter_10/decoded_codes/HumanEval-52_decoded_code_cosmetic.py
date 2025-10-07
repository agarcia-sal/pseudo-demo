from typing import List

def below_threshold(list_of_numbers: List[float], threshold: float) -> bool:
    iterator: int = 0
    while iterator < len(list_of_numbers):
        current_value: float = list_of_numbers[iterator]
        if not (current_value < threshold):
            return False
        iterator += 1
    return True