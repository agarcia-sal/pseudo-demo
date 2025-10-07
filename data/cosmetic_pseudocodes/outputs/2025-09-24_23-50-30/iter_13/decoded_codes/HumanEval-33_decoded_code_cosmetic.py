from typing import Sequence, List, TypeVar

T = TypeVar('T')

def sort_third(input_seq: Sequence[T]) -> List[T]:
    cloned_seq: List[T] = list(input_seq)
    targeted_positions: List[int] = []
    extracted_elems: List[T] = []
    for idx in range(len(cloned_seq)):
        if idx % 3 == 0:
            targeted_positions.append(idx)
            extracted_elems.append(cloned_seq[idx])
    sorted_elems = sorted(extracted_elems)
    for pos_idx, pos in enumerate(targeted_positions):
        cloned_seq[pos] = sorted_elems[pos_idx]
    return cloned_seq