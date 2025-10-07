from typing import List

def add_elements(arr: List[int], k: int) -> int:
    if k <= 0:
        return 0
    limit = min(k, len(arr))
    total = 0
    for element in arr[:limit]:
        if element == 0:
            digits = 1
        else:
            digits = len(str(abs(element)))
        if digits <= 2:
            total += element
    return total