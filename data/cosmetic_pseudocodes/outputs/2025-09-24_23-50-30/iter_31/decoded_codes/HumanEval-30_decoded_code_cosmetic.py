from typing import Iterable, List, Sequence, TypeVar

T = TypeVar('T', bound=float)

def get_positive(collection: Sequence[T]) -> List[T]:
    def select_positive(sequence: Sequence[T]) -> List[T]:
        if not sequence:
            return []
        head, *tail = sequence
        return ([head] if head > 0 else []) + select_positive(tail)
    return select_positive(collection)