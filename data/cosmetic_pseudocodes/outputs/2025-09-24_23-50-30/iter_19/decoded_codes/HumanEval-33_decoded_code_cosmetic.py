from typing import List, TypeVar

T = TypeVar('T')

def sort_third(array_data: List[T]) -> List[T]:
    duplicate_data: List[T] = [element for element in array_data]

    filtered_elements: List[T] = [duplicate_data[pos] for pos in range(len(duplicate_data)) if pos % 3 == 0]

    ordered_collection: List[T] = sorted(filtered_elements)

    pointer: int = 0
    for ix in range(len(duplicate_data)):
        if ix % 3 == 0:
            duplicate_data[ix] = ordered_collection[pointer]
            pointer += 1

    return duplicate_data