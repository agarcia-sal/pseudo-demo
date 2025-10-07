from typing import List


def below_threshold(list_of_numbers: List[float], threshold: float) -> bool:
    def check_elements(index: int) -> bool:
        if index == len(list_of_numbers):
            return True
        if threshold <= list_of_numbers[index]:
            return False
        return check_elements(index + 1)
    return check_elements(0)