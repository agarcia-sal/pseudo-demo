from typing import List

def maximum(numbers: List[int], count: int) -> List[int]:
    if count == 0:
        return []
    numbers.sort()
    return numbers[-count:]