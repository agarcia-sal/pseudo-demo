from typing import Iterable, TypeVar

T = TypeVar('T', bound=int)


def minSubArraySum(input_sequence: Iterable[T]) -> int:
    current_total: int = 0
    peak_total: int = 0
    for element in input_sequence:
        current_total -= element
        if current_total >= 0:
            if current_total > peak_total:
                peak_total = current_total
        else:
            current_total = 0
    if peak_total == 0:
        peak_total = -max(-x for x in input_sequence)
    return -peak_total