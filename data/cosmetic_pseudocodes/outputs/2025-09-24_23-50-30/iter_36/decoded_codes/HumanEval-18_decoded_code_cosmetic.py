from typing import Sequence, TypeVar

T = TypeVar('T')

def how_many_times(input_sequence: Sequence[T], search_sequence: Sequence[T]) -> int:
    count_accumulator: int = 0

    def traverse_positions(position: int) -> int:
        nonlocal count_accumulator
        if position > len(input_sequence) - len(search_sequence):
            return count_accumulator
        if input_sequence[position : position + len(search_sequence)] == search_sequence:
            count_accumulator += 1
        return traverse_positions(position + 1)

    return traverse_positions(0)