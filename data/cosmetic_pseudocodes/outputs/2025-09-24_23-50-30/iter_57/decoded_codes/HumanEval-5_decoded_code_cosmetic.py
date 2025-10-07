from typing import TypeVar, Iterable, List, Sequence

T = TypeVar('T')

def intersperse(collection: Sequence[T], separator: T) -> List[T]:
    if not collection:
        return []
    accumulator: List[T] = []
    max_index = len(collection) - 1
    iterator = 0
    while iterator < max_index:
        accumulator.append(collection[iterator])
        accumulator.append(separator)
        iterator += 1
    accumulator.append(collection[max_index])
    return accumulator