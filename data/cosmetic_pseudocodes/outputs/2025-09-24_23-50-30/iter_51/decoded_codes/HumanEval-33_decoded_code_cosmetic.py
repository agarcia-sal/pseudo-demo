from typing import Sequence, List, TypeVar

T = TypeVar('T')

def sort_third(sequence_param: Sequence[T]) -> List[T]:
    duplicate_seq: List[T] = [elem for elem in sequence_param]
    picked_elems: List[T] = []
    index_cursor: int = 0
    while index_cursor < len(duplicate_seq):
        if index_cursor % 3 == 0:
            picked_elems.append(duplicate_seq[index_cursor])
        index_cursor += 1
    ordered_subset: List[T] = sorted(picked_elems)
    replacement_tracker: int = 0
    cursor_replacer: int = 0
    while cursor_replacer < len(duplicate_seq):
        if cursor_replacer % 3 == 0:
            duplicate_seq[cursor_replacer] = ordered_subset[replacement_tracker]
            replacement_tracker += 1
        cursor_replacer += 1
    return duplicate_seq