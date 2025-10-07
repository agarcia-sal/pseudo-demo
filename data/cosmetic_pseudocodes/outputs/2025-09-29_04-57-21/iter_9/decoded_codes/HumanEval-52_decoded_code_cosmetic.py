from typing import List

def below_threshold(list_of_numbers: List[float], threshold: float) -> bool:
    index_counter: int = 0
    while index_counter < len(list_of_numbers):
        candidate: float = list_of_numbers[index_counter]
        if not (candidate < threshold):
            return False
        index_counter += 1
    return True