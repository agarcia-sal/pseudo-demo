from typing import List, TypeVar

T = TypeVar('T')

def intersperse(collection_of_values: List[T], div: T) -> List[T]:
    if not collection_of_values:
        return []
    accumulator: List[T] = []
    index = 0
    last_index = len(collection_of_values) - 1
    while index < last_index:
        current_value = collection_of_values[index]
        accumulator.append(current_value)
        accumulator.append(div)
        index += 1
    accumulator.append(collection_of_values[last_index])
    return accumulator