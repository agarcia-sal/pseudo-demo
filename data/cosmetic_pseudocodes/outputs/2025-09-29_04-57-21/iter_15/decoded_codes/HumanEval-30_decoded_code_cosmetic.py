from typing import Iterable, List

def get_positive(number_collection: Iterable[float]) -> List[float]:
    filtered_numbers: List[float] = []
    iterator: int = 0
    length: int = 0
    try:
        length = len(number_collection)  # try to get length if available
    except TypeError:
        # If no len(), convert to list for indexing
        number_collection = list(number_collection)
        length = len(number_collection)
    while iterator < length:
        if not (number_collection[iterator] <= 0):
            filtered_numbers.append(number_collection[iterator])
        iterator += 1
    return filtered_numbers