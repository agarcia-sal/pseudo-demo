from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    if numbers == []:
        return []
    result = []
    index = 0
    length = len(numbers) - 1
    while index < length:
        result.append(numbers[index])
        result.append(delimeter)
        index += 1
    result.append(numbers[index])
    return result