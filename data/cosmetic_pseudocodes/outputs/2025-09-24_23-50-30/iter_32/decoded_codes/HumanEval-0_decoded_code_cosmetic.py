from typing import List


def has_close_elements(list_of_numbers: List[float], threshold_value: float) -> bool:
    x0: int = len(list_of_numbers)
    y1: int = 0
    while y1 < x0:
        z2: int = 0
        while z2 < x0:
            if y1 != z2:
                w3: float = list_of_numbers[y1] - list_of_numbers[z2]
                if w3 < 0:
                    w3 = -w3
                if w3 < threshold_value:
                    return True
            z2 += 1
        y1 += 1
    return False