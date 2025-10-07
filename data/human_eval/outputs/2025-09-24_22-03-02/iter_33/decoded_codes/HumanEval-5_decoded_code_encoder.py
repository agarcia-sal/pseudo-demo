from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    if numbers == []:
        return []
    result = []
    last_index = len(numbers) - 1
    index = 0
    while index < last_index:
        result.append(numbers[index])
        result.append(delimeter)
        index += 1
    result.append(numbers[last_index])
    return result