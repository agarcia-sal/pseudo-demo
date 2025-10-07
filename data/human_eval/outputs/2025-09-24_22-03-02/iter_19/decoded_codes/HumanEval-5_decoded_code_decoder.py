from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    if not numbers:
        return []
    result: List[int] = []
    length = len(numbers)
    last_index = length - 1
    for index in range(last_index):
        result.append(numbers[index])
        result.append(delimeter)
    result.append(numbers[last_index])
    return result