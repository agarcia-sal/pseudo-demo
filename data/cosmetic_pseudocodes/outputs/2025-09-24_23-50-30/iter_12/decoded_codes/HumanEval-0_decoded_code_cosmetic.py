from typing import List

def has_close_elements(list_of_numbers: List[float], threshold_value: float) -> bool:
    length = len(list_of_numbers)
    for outer_pointer in range(length):
        for inner_pointer in range(length):
            if outer_pointer != inner_pointer:
                gap = list_of_numbers[outer_pointer] - list_of_numbers[inner_pointer]
                dist = -gap if gap < 0 else gap
                if dist < threshold_value:
                    return True
    return False