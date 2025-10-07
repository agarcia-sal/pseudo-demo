from typing import Sequence, TypeVar, List

T = TypeVar('T')

def intersperse(p_sequence: Sequence[T], p_divider: T) -> List[T]:
    if not p_sequence:
        return []
    r_output: List[T] = []
    idx_counter = 0
    last_idx = len(p_sequence) - 1
    while idx_counter < last_idx:
        current_val = p_sequence[idx_counter]
        r_output.append(current_val)
        r_output.append(p_divider)
        idx_counter += 1
    final_element = p_sequence[last_idx]
    r_output.append(final_element)
    return r_output