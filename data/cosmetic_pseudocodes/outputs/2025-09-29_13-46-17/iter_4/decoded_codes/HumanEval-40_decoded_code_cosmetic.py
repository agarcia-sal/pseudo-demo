from typing import List


def triples_sum_to_zero(list_of_integers: List[int]) -> bool:
    def check_triplet_positions(pos_a: int, pos_b: int, pos_c: int) -> bool:
        if pos_a >= len(list_of_integers) - 2:
            return False
        if pos_b >= len(list_of_integers) - 1:
            return check_triplet_positions(pos_a + 1, pos_a + 2, pos_a + 3)
        if pos_c >= len(list_of_integers):
            return check_triplet_positions(pos_a, pos_b + 1, pos_b + 2)
        if list_of_integers[pos_a] + list_of_integers[pos_b] + list_of_integers[pos_c] == 0:
            return True
        return check_triplet_positions(pos_a, pos_b, pos_c + 1)

    return check_triplet_positions(0, 1, 2)