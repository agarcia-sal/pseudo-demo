from typing import List

def eat(value: int, required: int, available: int) -> List[int]:
    if required <= available:
        return [value + required, available - required]
    else:
        return [value + available, 0]