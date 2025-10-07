from typing import List

def has_close_elements(list_of_numbers: List[float], threshold_value: float) -> bool:
    length = len(list_of_numbers)
    for posA in range(length):
        for posB in range(length):
            if posA == posB:
                continue
            delta = list_of_numbers[posA] - list_of_numbers[posB]
            if -threshold_value < delta < threshold_value:
                return True
    return False