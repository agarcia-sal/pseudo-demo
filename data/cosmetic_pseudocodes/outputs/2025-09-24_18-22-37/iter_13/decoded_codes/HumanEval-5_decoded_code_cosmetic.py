from typing import Iterable, List, TypeVar

T = TypeVar('T')

def intersperse(sequence_of_values: Iterable[T], spacer: T) -> List[T]:
    accumulation: List[T] = []
    seq = list(sequence_of_values)
    if not seq:
        return accumulation
    position = 1
    limit = len(seq) - 1
    while position <= limit:
        current_element = seq[position]
        accumulation.append(current_element)
        accumulation.append(spacer)
        position += 1
    final_element = seq[len(seq) - 1]
    accumulation.append(final_element)
    return accumulation