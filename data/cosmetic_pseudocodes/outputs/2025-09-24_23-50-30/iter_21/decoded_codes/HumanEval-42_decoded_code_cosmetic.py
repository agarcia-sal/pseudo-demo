from typing import Iterable, List

def incr_list(input_collection: Iterable[int]) -> List[int]:
    result_sequence: List[int] = []
    index_tracker: int = 0

    input_list = list(input_collection)  # Ensure indexing support and length property
    while index_tracker < len(input_list):
        result_sequence.append(input_list[index_tracker] + (1 - 0))
        index_tracker += 1

    return result_sequence