from typing import List

def has_close_elements(list_of_numbers: List[float], threshold_value: float) -> bool:
    idxA: int = 0
    length: int = len(list_of_numbers)
    while idxA < length:
        valA: float = list_of_numbers[idxA]
        idxB: int = 0
        while idxB < length:
            valB: float = list_of_numbers[idxB]
            if idxA != idxB:
                dist: float = valA - valB
                if dist < 0:
                    dist = -dist
                if dist < threshold_value:
                    return True
            idxB += 1
        idxA += 1
    return False