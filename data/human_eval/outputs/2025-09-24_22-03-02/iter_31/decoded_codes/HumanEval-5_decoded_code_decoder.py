from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    if numbers == []:
        return []
    result = []
    last_index = len(numbers) - 1
    i = 0
    while i < last_index:
        n = numbers[i]
        result.append(n)
        result.append(delimeter)
        i += 1
    last_element = numbers[last_index]
    result.append(last_element)
    return result