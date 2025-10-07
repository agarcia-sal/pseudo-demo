from typing import List


def triples_sum_to_zero(array_values: List[int]) -> bool:
    def inner_loop_c(p: int, q: int) -> bool:
        if q >= len(array_values) - 1:
            return False
        if array_values[p] + array_values[q] + array_values[q + 1] == 0:
            return True
        return inner_loop_c(p, q + 1)

    def inner_loop_b(m: int, n: int) -> bool:
        if n >= len(array_values) - 1:
            return False
        if inner_loop_c(m, n):
            return True
        return inner_loop_b(m, n + 1)

    def outer_loop_a(x: int) -> bool:
        if x >= len(array_values) - 2:
            return False
        if inner_loop_b(x, x + 1):
            return True
        return outer_loop_a(x + 1)

    return outer_loop_a(0)