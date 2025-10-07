from typing import Iterable, List, TypeVar

T = TypeVar('T', bound=float)  # Assuming comparable numeric types

def get_positive(input_sequence: Iterable[T]) -> List[T]:
    return [each_item for each_item in input_sequence if each_item > 0]