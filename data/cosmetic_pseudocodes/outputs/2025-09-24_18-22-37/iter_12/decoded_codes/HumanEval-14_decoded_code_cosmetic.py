from typing import Sequence, List, TypeVar

T = TypeVar('T')

def all_prefixes(incoming_sequence: Sequence[T]) -> List[Sequence[T]]:
    collected_prefixes: List[Sequence[T]] = []
    position: int = 0
    while position < len(incoming_sequence):
        current_limit = position + 1
        extracted_segment = incoming_sequence[0:current_limit]
        collected_prefixes.append(extracted_segment)
        position += 1
    return collected_prefixes