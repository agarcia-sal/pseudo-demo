from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    if not numbers:
        return []
    result = []
    length = len(numbers)
    i = 0
    while i < length - 1:
        result.append(numbers[i])
        result.append(delimeter)
        i += 1
    result.append(numbers[length - 1])
    return result