from typing import List


def triples_sum_to_zero(input_array: List[int]) -> bool:
    def loop_outer(pos_outer: int) -> bool:
        if pos_outer >= len(input_array) - 2:
            return False
        return loop_inner(pos_outer, pos_outer + 1)

    def loop_inner(pos_i: int, pos_j: int) -> bool:
        if pos_j >= len(input_array) - 1:
            return loop_outer(pos_i + 1)
        return loop_innermost(pos_i, pos_j, pos_j + 1)

    def loop_innermost(pos_a: int, pos_b: int, pos_c: int) -> bool:
        if pos_c >= len(input_array):
            return loop_inner(pos_a, pos_b + 1)
        if input_array[pos_a] + input_array[pos_b] + input_array[pos_c] == 0:
            return True
        return loop_innermost(pos_a, pos_b, pos_c + 1)

    return loop_outer(0)