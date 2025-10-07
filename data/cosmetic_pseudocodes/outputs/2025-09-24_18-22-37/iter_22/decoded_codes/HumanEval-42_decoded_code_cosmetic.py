from typing import Sequence, List

def incr_list(sequence: Sequence[int]) -> List[int]:
    result_container: List[int] = []
    index_counter: int = 0
    while index_counter < len(sequence):
        current_value: int = sequence[index_counter]
        incremented_value: int = current_value + 1
        result_container.append(incremented_value)
        index_counter += 1
    return result_container