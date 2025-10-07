from typing import Sequence, TypeVar, Union

TNum = TypeVar('TNum', int, float)


def median(sequence: Sequence[TNum]) -> Union[TNum, float]:
    ordered_seq = sorted(sequence)
    size = len(ordered_seq)
    if size % 2 != 0:
        return ordered_seq[size // 2]
    else:
        idx = size // 2
        return (ordered_seq[idx - 1] + ordered_seq[idx]) * 0.5