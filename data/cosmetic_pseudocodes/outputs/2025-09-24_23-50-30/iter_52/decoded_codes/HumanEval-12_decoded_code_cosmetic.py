from typing import Sequence, Optional, TypeVar

T = TypeVar('T', bound=Sequence)

def longest(input_sequence: Sequence[T]) -> Optional[T]:
    if len(input_sequence) == 0:
        return None

    def find_max_len(seq: Sequence[T], current_best: int) -> int:
        if len(seq) == 0:
            return current_best
        head_element = seq[0]
        tail_seq = seq[1:]
        head_length = len(head_element)
        next_best = current_best
        if head_length > current_best:
            next_best = head_length
        return find_max_len(tail_seq, next_best)

    total_max_length = find_max_len(input_sequence, 0)

    def search_for_len(seq: Sequence[T], target_length: int) -> Optional[T]:
        if len(seq) == 0:
            return None
        head_element = seq[0]
        tail_seq = seq[1:]
        if len(head_element) == target_length:
            return head_element
        return search_for_len(tail_seq, target_length)

    return search_for_len(input_sequence, total_max_length)