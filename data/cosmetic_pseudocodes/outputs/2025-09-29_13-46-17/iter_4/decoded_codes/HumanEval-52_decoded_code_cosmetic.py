from typing import List

def below_threshold(list_of_numbers: List[float], threshold: float) -> bool:
    def helper(index: int) -> bool:
        if index == len(list_of_numbers):
            return True
        if not (list_of_numbers[index] < threshold):
            return False
        return helper(index + 1)
    return helper(0)