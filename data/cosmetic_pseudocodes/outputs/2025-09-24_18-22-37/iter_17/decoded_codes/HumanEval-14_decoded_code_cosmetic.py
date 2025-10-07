from typing import Sequence, List, TypeVar

T = TypeVar('T')

def all_prefixes(original_seq: Sequence[T]) -> List[Sequence[T]]:
    collected: List[Sequence[T]] = []
    cursor: int = 0
    while cursor < len(original_seq):
        chunk_length = cursor + 1
        fragment = original_seq[:chunk_length]
        collected.append(fragment)
        cursor += 1
    return collected