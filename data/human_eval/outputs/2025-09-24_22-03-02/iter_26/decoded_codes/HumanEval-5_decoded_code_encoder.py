from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    if len(numbers) == 0:
        return []
    result = []
    index = 0
    upper_bound = len(numbers) - 2
    while index <= upper_bound:
        n = numbers[index]
        result.append(n)
        result.append(delimeter)
        index += 1
    last_element = numbers[len(numbers) - 1]
    result.append(last_element)
    return result