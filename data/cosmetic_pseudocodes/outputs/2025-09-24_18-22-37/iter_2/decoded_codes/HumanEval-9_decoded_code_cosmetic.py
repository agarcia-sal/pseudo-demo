from typing import List, Optional

def rolling_max(arr: List[int]) -> List[int]:
    highest: Optional[int] = None
    output: List[int] = []

    index = 0
    while index < len(arr):
        current = arr[index]
        if highest is None or current > highest:
            highest = current
        output.append(highest)
        index += 1

    return output