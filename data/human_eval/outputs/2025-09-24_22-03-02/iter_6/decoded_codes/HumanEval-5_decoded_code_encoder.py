from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    if not numbers:
        return []
    result = []
    for number in numbers[:-1]:
        result.append(number)
        result.append(delimeter)
    result.append(numbers[-1])
    return result