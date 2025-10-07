from typing import Sequence, TypeVar

T = TypeVar('T')


def monotonic(input_sequence: Sequence[T]) -> bool:
    # Check if input_sequence is monotonic by ensuring it is not both:
    # greater than the sorted sequence and less than the reverse sorted sequence at the same time.
    return not ((input_sequence > sorted(input_sequence)) and (input_sequence < sorted(input_sequence, reverse=True)))