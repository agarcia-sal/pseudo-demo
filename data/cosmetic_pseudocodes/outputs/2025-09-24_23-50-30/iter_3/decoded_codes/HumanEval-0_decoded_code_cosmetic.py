from typing import List


def has_close_elements(list_of_numbers: List[float], threshold_value: float) -> bool:
    size = len(list_of_numbers)
    for i in range(size):
        for j in range(size):
            if i != j:
                gap = list_of_numbers[i] - list_of_numbers[j]
                if gap < 0:
                    gap = -gap
                if gap < threshold_value:
                    return True
    return False