from typing import Sequence, List, TypeVar

T = TypeVar('T')

def strange_sort_list(input_sequence: Sequence[T]) -> List[T]:
    seq = list(input_sequence)
    output_sequence: List[T] = []
    toggle_indicator = False
    while seq:
        if not toggle_indicator:
            chosen_element = min(seq)
        else:
            chosen_element = max(seq)
        output_sequence.append(chosen_element)
        seq.remove(chosen_element)
        toggle_indicator = not toggle_indicator
    return output_sequence