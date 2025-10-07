from typing import Sequence, TypeVar

T = TypeVar('T', bound=Sequence)

def total_match(sequence_alpha: Sequence[T], sequence_beta: Sequence[T]) -> Sequence[T]:
    def sum_lengths(collection: Sequence[T]) -> int:
        accumulator = 0
        for item in collection:
            accumulator += len(item)
        return accumulator

    measure_alpha = sum_lengths(sequence_alpha)
    measure_beta = sum_lengths(sequence_beta)

    if measure_alpha <= measure_beta:
        return sequence_alpha
    else:
        return sequence_beta