from typing import List

def below_threshold(list_of_numbers: List[float], threshold: float) -> bool:
    def check(idx: int) -> bool:
        if idx == len(list_of_numbers):
            return True
        val = list_of_numbers[idx]
        if not (val < threshold):
            return False
        return check(idx + 1)
    return check(0)