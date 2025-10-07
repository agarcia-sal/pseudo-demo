from typing import Sequence, List

def incr_list(collection_sequence: Sequence[int]) -> List[int]:
    temp_collection: List[int] = []
    index_counter: int = 0

    while index_counter < len(collection_sequence):
        temp_collection.append(collection_sequence[index_counter] + 1)
        index_counter += 1

    return temp_collection