from typing import List

def below_threshold(list_of_numbers: List[float], threshold: float) -> bool:
    def checkItem(idx: int) -> bool:
        if idx == len(list_of_numbers):
            return True
        currentValue = list_of_numbers[idx]
        if currentValue >= threshold:
            return False
        return checkItem(idx + 1)
    return checkItem(0)