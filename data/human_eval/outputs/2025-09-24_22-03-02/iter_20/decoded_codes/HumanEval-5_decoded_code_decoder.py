from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    if not numbers:
        return []
    result: List[int] = []
    index = 0
    while index < len(numbers) - 1:
        result.append(numbers[index])
        result.append(delimiter)
        index += 1
    result.append(numbers[-1])
    return result