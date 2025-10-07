from collections import Counter
from typing import Sequence, List, TypeVar

T = TypeVar('T')

def remove_duplicates(sequence_input: Sequence[T]) -> List[T]:
    tally_map = Counter(sequence_input)
    filtered_collection: List[T] = [
        token for token in sequence_input if tally_map[token] <= 1
    ]
    return filtered_collection