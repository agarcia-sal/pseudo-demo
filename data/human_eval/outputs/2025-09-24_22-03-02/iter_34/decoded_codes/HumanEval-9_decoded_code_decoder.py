from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    running_max = None
    result = []
    for n in numbers:
        if running_max is None:
            running_max = n
        else:
            running_max = running_max if running_max > n else n
        result.append(running_max)
    return result