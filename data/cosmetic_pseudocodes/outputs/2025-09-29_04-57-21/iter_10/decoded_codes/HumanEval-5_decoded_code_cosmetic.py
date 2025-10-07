from typing import List

def intersperse(list_of_numbers: List[int], delimiter: int) -> List[int]:
    if not list_of_numbers:
        return []

    outcome: List[int] = []
    position: int = 0
    max_index: int = len(list_of_numbers) - 1

    while position < max_index:
        element = list_of_numbers[position]
        outcome.append(element)
        outcome.append(delimiter)
        position += 1

    outcome.append(list_of_numbers[max_index])
    return outcome