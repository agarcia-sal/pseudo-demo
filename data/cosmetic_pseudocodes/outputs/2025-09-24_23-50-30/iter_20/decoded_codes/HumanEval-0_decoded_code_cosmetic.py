from typing import List

def has_close_elements(list_of_numbers: List[float], threshold_value: float) -> bool:
    n = len(list_of_numbers)
    for i in range(n):
        for j in range(n):
            if i != j:
                delta = abs(list_of_numbers[i] - list_of_numbers[j])
                if delta < threshold_value:
                    return True
    return False