from typing import List


def has_close_elements(list_of_numbers: List[float], threshold_value: float) -> bool:
    length = len(list_of_numbers)
    for i in range(length):
        for j in range(length):
            if i != j:
                if abs(list_of_numbers[i] - list_of_numbers[j]) < threshold_value:
                    return True
    return False