from typing import List, TypeVar

T = TypeVar("T")  # generic type for sequence values
S = TypeVar("S")  # generic type for separator marker

def intersperse(sequence_values: List[T], sep_marker: S) -> List[T | S]:
    def recursive_build(index_pos: int, acc_array: List[T | S]) -> List[T | S]:
        if index_pos == len(sequence_values):
            return acc_array
        elif index_pos == len(sequence_values) - 1:
            return acc_array + [sequence_values[index_pos]]
        else:
            return recursive_build(index_pos + 1, acc_array + [sequence_values[index_pos], sep_marker])

    if len(sequence_values) == 0:
        return []
    else:
        return recursive_build(0, [])