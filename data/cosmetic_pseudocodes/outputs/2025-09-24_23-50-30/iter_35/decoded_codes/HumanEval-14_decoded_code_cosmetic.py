from typing import Sequence, List, TypeVar

T = TypeVar('T')

def all_prefixes(mystery_sequence: Sequence[T]) -> List[Sequence[T]]:
    output_collection: List[Sequence[T]] = []
    loop_index: int = 0
    while loop_index < len(mystery_sequence):
        output_collection.append(mystery_sequence[:loop_index + 1])
        loop_index += 1
    return output_collection