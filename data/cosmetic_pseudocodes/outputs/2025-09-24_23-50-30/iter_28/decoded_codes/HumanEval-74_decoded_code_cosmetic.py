from typing import Sequence, Union

def total_match(prmA: Sequence[Sequence], prmB: Sequence[Sequence]) -> Sequence[Sequence]:
    def sum_length(seq: Sequence[Sequence], idx: int, acc: int) -> int:
        if idx == len(seq):
            return acc
        else:
            return sum_length(seq, idx + 1, acc + len(seq[idx]))

    totalA = sum_length(prmA, 0, 0)
    totalB = sum_length(prmB, 0, 0)

    if totalA <= totalB:
        return prmA
    else:
        return prmB