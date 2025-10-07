from typing import Sequence

def solution(list_of_integers: Sequence[int]) -> int:
    def accumulate_odd_at_even_indices(sequence: Sequence[int], position: int) -> int:
        if position >= len(sequence):
            return 0
        if position % 2 == 0 and sequence[position] % 2 != 0:
            return sequence[position] + accumulate_odd_at_even_indices(sequence, position + 1)
        else:
            return accumulate_odd_at_even_indices(sequence, position + 1)

    return accumulate_odd_at_even_indices(list_of_integers, 0)