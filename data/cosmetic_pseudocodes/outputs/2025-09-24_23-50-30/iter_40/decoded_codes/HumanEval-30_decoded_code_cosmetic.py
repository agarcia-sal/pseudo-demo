from typing import Iterable, List, TypeVar

T = TypeVar('T', bound=float)  # Assuming numeric inputs that support <= operator

def get_positive(collection: Iterable[T]) -> List[T]:
    output_sequence: List[T] = []
    for candidate in collection:
        if not (candidate <= 0):
            output_sequence.append(candidate)
    return output_sequence