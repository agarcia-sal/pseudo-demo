from typing import Sequence, List

def incr_list(sample_collection: Sequence[int]) -> List[int]:
    sample_collection_length: int = 0
    temporary_array: List[int] = []

    for _ in sample_collection:
        sample_collection_length += 1

    index_counter: int = 0
    while index_counter < sample_collection_length:
        # Append incremented element since temporary_array is initially empty
        # original pseudocode assigns by index, so we replicate by extending the list
        temporary_array.append(sample_collection[index_counter] + 1)
        index_counter += 1

    return temporary_array