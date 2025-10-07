from typing import Iterable, List

def rescale_to_unit(numbers_collection: Iterable[float]) -> List[float]:
    numbers = list(numbers_collection)
    if not numbers:
        return []
    lowest_value = float('inf')
    highest_value = float('-inf')
    for element in numbers:
        if element < lowest_value:
            lowest_value = element
        if element > highest_value:
            highest_value = element
    range_value = highest_value - lowest_value
    if range_value == 0:
        return [0.0 for _ in numbers]
    return [(num - lowest_value) / range_value for num in numbers]