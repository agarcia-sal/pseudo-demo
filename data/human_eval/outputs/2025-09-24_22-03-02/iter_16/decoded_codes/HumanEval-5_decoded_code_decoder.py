from typing import List, Optional

def intersperse(numbers: List[Optional[int]], delimeter: int) -> List[Optional[int]]:
    if numbers == [None]:
        return [None]
    result: List[Optional[int]] = []
    for n in numbers[:-1]:
        result.append(n)
        result.append(delimeter)
    result.append(numbers[-1])
    return result