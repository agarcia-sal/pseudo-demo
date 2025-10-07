from typing import Iterable, List, TypeVar

T = TypeVar('T', bound=float)  # assuming numeric types for comparison with 0

def get_positive(input_collection: Iterable[T]) -> List[T]:
    output_accumulator: List[T] = []
    for intermediate_element in input_collection:
        if intermediate_element > 0:
            output_accumulator.append(intermediate_element)
    return output_accumulator