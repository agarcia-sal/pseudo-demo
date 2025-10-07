from typing import Sequence, List, Union

def filter_integers(input_sequence: Sequence[object]) -> List[int]:
    def recursive_filter(sequence: Sequence[object], index: int, accumulator: List[int]) -> List[int]:
        if index == len(sequence):
            return accumulator
        element = sequence[index]
        if not isinstance(element, int):
            return recursive_filter(sequence, index + 1, accumulator)
        updated_accumulator = accumulator + [element]
        return recursive_filter(sequence, index + 1, updated_accumulator)
    return recursive_filter(input_sequence, 0, [])