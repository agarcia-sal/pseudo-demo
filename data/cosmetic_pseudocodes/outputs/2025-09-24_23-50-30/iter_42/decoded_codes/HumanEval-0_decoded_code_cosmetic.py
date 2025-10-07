from typing import Sequence


def has_close_elements(array_of_values: Sequence[int], limit: int) -> bool:
    def search_pair(pos_a: int, pos_b: int) -> bool:
        if pos_a >= len(array_of_values):
            return False
        if pos_b >= len(array_of_values):
            return search_pair(pos_a + 1, 0)
        if pos_a == pos_b:
            return search_pair(pos_a, pos_b + 1)
        delta = array_of_values[pos_a] - array_of_values[pos_b]
        if abs(delta) < limit:
            return True
        return search_pair(pos_a, pos_b + 1)

    return search_pair(0, 0)