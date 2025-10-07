from typing import Sequence, List, TypeVar

T = TypeVar('T', bound=float)

def get_positive(input_collection: Sequence[T]) -> List[T]:
    output_collection: List[T] = []
    for index in range(len(input_collection)):
        current_item = input_collection[index]
        if current_item > 0:
            output_collection.append(current_item)
    return output_collection