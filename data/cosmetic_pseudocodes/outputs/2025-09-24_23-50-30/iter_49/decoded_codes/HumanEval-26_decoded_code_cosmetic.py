from collections import Counter
from typing import List, TypeVar

T = TypeVar('T')

def remove_duplicates(sequence_data: List[T]) -> List[T]:
    count_map: Counter[T] = Counter(sequence_data)

    def filter_unique(input_seq: List[T], index_acc: int, result_accum: List[T]) -> List[T]:
        if index_acc >= len(input_seq):
            return result_accum
        current_val = input_seq[index_acc]
        if count_map[current_val] > 1:
            return filter_unique(input_seq, index_acc + 1, result_accum)
        return filter_unique(input_seq, index_acc + 1, result_accum + [current_val])

    return filter_unique(sequence_data, 0, [])