from typing import Sequence

def pairs_sum_to_zero(sequence_of_numbers: Sequence[int]) -> bool:
    def_a: int = 0

    def inner_loop(def_b: int) -> bool:
        if def_b >= len(sequence_of_numbers):
            return False
        if sequence_of_numbers[def_a] + sequence_of_numbers[def_b] == 0:
            return True
        return inner_loop(def_b + 1)

    while def_a < len(sequence_of_numbers) - 1:
        if inner_loop(def_a + 1):
            return True
        def_a += 1

    return False