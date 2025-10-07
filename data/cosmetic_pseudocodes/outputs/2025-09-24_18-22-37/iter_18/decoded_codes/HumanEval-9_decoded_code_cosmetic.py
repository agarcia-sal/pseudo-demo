from typing import Sequence, List, Optional, TypeVar

T = TypeVar('T', bound=float)


def rolling_max(input_seq: Sequence[T]) -> List[T]:
    curr_peak: Optional[T] = None
    output_sequence: List[T] = []

    idx: int = 0
    while idx < len(input_seq):
        val: T = input_seq[idx]
        if curr_peak is None:
            curr_peak = val
        else:
            if curr_peak < val:
                curr_peak = val
        output_sequence.append(curr_peak)
        idx += 1

    return output_sequence