from typing import Sequence, TypeVar

T = TypeVar('T', bound=Sequence)

def total_match(sequence_alpha: Sequence[Sequence], sequence_beta: Sequence[Sequence]) -> Sequence[Sequence]:
    def sum_lengths(coll: Sequence[Sequence], acc: int) -> int:
        if not coll:
            return acc
        return sum_lengths(coll[1:], acc + len(coll[0]))

    total_alpha = sum_lengths(sequence_alpha, 0)
    total_beta = sum_lengths(sequence_beta, 0)

    if total_alpha <= total_beta:
        return sequence_alpha
    else:
        return sequence_beta