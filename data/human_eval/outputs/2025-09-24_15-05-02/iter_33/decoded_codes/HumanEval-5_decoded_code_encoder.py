from typing import List

def intersperse(list_of_numbers: List[int], delimiter: int) -> List[int]:
    if not list_of_numbers:
        return []
    result: List[int] = []
    for number in list_of_numbers[:-1]:
        result.append(number)
        result.append(delimiter)
    result.append(list_of_numbers[-1])
    return result