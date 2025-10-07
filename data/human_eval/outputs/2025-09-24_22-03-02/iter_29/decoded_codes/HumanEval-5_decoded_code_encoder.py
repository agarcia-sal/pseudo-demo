from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    if not numbers:
        return []
    result = []
    last_index = len(numbers) - 2
    for i in range(last_index + 1):
        result.append(numbers[i])
        result.append(delimeter)
    result.append(numbers[-1])
    return result