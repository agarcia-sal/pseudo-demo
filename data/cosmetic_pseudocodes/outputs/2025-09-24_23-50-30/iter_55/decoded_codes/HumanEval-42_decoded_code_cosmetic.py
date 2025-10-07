from typing import Sequence, List

def incr_list(input_sequence: Sequence[int]) -> List[int]:
    def add_one_recursive(source_seq: Sequence[int], index: int, accumulator: List[int]) -> List[int]:
        if index == len(source_seq):
            return accumulator
        updated_accumulator = accumulator + [source_seq[index] + 1]
        return add_one_recursive(source_seq, index + 1, updated_accumulator)
    return add_one_recursive(input_sequence, 0, [])