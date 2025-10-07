from typing import List, Optional

def rolling_max(numbers: List[int]) -> List[int]:
    running_max: Optional[int] = None
    result: List[int] = []

    index = 0
    while index < len(numbers):
        n = numbers[index]
        if running_max is None:
            running_max = n
        else:
            if running_max > n:
                running_max = running_max
            else:
                running_max = n
        result.append(running_max)
        index += 1

    return result