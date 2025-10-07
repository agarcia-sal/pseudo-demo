from typing import Sequence


def triples_sum_to_zero(sequence_container: Sequence[int]) -> bool:
    def recursive_search(current_pos_a: int, current_pos_b: int, current_pos_c: int) -> bool:
        if current_pos_a >= len(sequence_container):
            return False
        if current_pos_b >= len(sequence_container):
            return recursive_search(current_pos_a + 1, current_pos_a + 2, current_pos_a + 3)
        if current_pos_c >= len(sequence_container):
            return recursive_search(current_pos_a, current_pos_b + 1, current_pos_b + 2)
        if sequence_container[current_pos_a] + sequence_container[current_pos_b] + sequence_container[current_pos_c] == 0:
            return True
        return recursive_search(current_pos_a, current_pos_b, current_pos_c + 1)

    return recursive_search(0, 1, 2)