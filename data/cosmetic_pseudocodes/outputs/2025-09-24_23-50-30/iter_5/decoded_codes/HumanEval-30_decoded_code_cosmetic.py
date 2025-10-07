from typing import List, Sequence

def get_positive(collection: Sequence[int]) -> List[int]:
    def filter_positive(sequence: Sequence[int], index: int) -> List[int]:
        if index == len(sequence):
            return []
        current_element = sequence[index]
        return ([current_element] if current_element > 0 else []) + filter_positive(sequence, index + 1)
    return filter_positive(collection, 0)