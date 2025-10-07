from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    if not numbers:
        return []
    result = []
    last_index = len(numbers) - 1
    for index in range(last_index):
        result.append(numbers[index])
        result.append(delimeter)
    result.append(numbers[last_index])
    return result