from typing import List

def has_close_elements(list_of_numbers: List[float], threshold_value: float) -> bool:
    length = len(list_of_numbers)
    for i in range(length):
        for j in range(length):
            if i != j:
                delta = list_of_numbers[i] - list_of_numbers[j]
                if (0 <= delta < threshold_value) or (delta < 0 and -delta < threshold_value):
                    return True
    return False