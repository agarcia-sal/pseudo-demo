from typing import Iterable, List, Optional

def rolling_max(numbers: Iterable[int]) -> List[int]:
    running_max: Optional[int] = None
    result: List[int] = []
    for n in numbers:
        if running_max is None:
            running_max = n
        else:
            running_max = max(running_max, n)
        result.append(running_max)
    return result