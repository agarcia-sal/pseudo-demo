from typing import List, Sequence

def incr_list(input_sequence: Sequence[int]) -> List[int]:
    def internal_increment(current_index: int, accumulated_result: List[int]) -> List[int]:
        if current_index == len(input_sequence):
            return accumulated_result
        new_accumulated_result = accumulated_result + [input_sequence[current_index] + 1]
        return internal_increment(current_index + 1, new_accumulated_result)
    return internal_increment(0, [])