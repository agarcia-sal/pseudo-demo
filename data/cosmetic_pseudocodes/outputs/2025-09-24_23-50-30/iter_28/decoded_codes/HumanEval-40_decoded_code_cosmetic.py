from typing import List


def triples_sum_to_zero(array_values: List[int]) -> bool:
    length_val: int = len(array_values)

    def check_triplets(pos_a: int, pos_b: int) -> bool:
        if pos_a >= length_val - 2:
            return False

        def inner_loop(pos_c: int) -> bool:
            if pos_c >= length_val:
                return check_triplets(pos_a + 1, pos_a + 2)
            if (array_values[pos_a] + array_values[pos_b] + array_values[pos_c]) == 0:
                return True
            return inner_loop(pos_c + 1)

        if pos_b >= length_val - 1:
            return check_triplets(pos_a + 1, pos_a + 2)
        return inner_loop(pos_b + 1)

    return check_triplets(0, 1)