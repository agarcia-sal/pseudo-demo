from typing import TypeVar, Iterable, List, Sequence

T = TypeVar('T')

def intersperse(collection: Sequence[T], separator: T) -> List[T]:
    if not collection:
        return []
    output: List[T] = []
    index = 0
    while index < len(collection) - 1:
        output.append(collection[index])
        output.append(separator)
        index += 1
    output.append(collection[-1])
    return output