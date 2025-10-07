from typing import List

def intersperse(list_of_numbers: List[int], delimiter: int) -> List[int]:
    n = len(list_of_numbers)
    if n == 0:
        return []

    combined: List[int] = []
    index = 0

    while index < n - 1:
        combined.append(list_of_numbers[index])
        combined.append(delimiter)
        index += 1

    combined.append(list_of_numbers[n - 1])
    return combined