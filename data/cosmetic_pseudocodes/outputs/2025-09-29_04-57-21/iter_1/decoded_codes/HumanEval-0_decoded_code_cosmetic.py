from typing import List

def has_close_elements(list_of_numbers: List[float], threshold_value: float) -> bool:
    for i in range(len(list_of_numbers)):
        for j in range(len(list_of_numbers)):
            if i != j:
                difference = list_of_numbers[i] - list_of_numbers[j]
                if difference < 0:
                    difference = -difference
                if difference < threshold_value:
                    return True
    return False