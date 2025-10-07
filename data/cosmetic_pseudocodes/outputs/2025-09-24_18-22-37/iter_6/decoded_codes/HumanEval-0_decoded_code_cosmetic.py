from typing import List

def has_close_elements(list_of_numbers: List[float], threshold_value: float) -> bool:
    p: int = 0
    length: int = len(list_of_numbers)
    while p < length:
        a: float = list_of_numbers[p]
        q: int = 0
        while q < length:
            if p == q:
                q += 1
                continue
            b: float = list_of_numbers[q]
            diff: float = a - b
            if diff < 0:
                diff = -diff
            if diff < threshold_value:
                return True
            q += 1
        p += 1
    return False