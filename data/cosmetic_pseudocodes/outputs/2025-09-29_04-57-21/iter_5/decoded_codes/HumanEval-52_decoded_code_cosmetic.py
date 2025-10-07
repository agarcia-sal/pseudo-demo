from typing import List

def below_threshold(list_of_numbers: List[float], threshold: float) -> bool:
    index: int = 0
    while not (index >= len(list_of_numbers)):
        analysis: float = list_of_numbers[index]
        if not (analysis < threshold):
            return False
        index += 1
    return True