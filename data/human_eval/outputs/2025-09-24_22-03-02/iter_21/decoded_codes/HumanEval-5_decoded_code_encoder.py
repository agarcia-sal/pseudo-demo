from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    if not numbers:
        return []
    result = []
    for index in range(len(numbers) - 1):
        result.append(numbers[index])
        result.append(delimeter)
    result.append(numbers[-1])
    return result