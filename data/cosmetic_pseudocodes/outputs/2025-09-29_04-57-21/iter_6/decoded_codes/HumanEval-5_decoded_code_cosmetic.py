from typing import Iterable, List, TypeVar

T = TypeVar('T')

def intersperse(sequence: List[T], sep: T) -> List[T]:
    if not sequence:
        return []
    output_collection: List[T] = []
    for index in range(len(sequence) - 1):
        output_collection.append(sequence[index])
        output_collection.append(sep)
    output_collection.append(sequence[-1])
    return output_collection