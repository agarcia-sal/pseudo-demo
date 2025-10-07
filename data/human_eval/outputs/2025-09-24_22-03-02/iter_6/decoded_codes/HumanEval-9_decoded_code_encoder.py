from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    running_max = None
    result = []
    for number in numbers:
        if running_max is None:
            running_max = number
        else:
            running_max = max(running_max, number)
        result.append(running_max)
    return result