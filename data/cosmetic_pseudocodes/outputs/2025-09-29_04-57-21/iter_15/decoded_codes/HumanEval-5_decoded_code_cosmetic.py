from typing import List

def intersperse(list_of_numbers: List[int], delimiter: int) -> List[int]:
    if not list_of_numbers:
        return []

    aggregated: List[int] = []
    idx: int = 0
    while idx < len(list_of_numbers) - 1:
        current_value = list_of_numbers[idx]
        aggregated.append(current_value)
        aggregated.append(delimiter)
        idx += 1

    aggregated.append(list_of_numbers[-1])
    return aggregated