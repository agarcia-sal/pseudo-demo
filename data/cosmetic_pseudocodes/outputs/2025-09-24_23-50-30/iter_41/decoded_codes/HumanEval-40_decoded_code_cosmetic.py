from typing import Sequence

def triples_sum_to_zero(container: Sequence[int]) -> bool:
    def inner_loop_c(x: int, y: int, z: int) -> bool:
        if z >= len(container):
            return inner_loop_b(x, y + 1)
        if container[x] + container[y] + container[z] == 0:
            return True
        return inner_loop_c(x, y, z + 1)

    def inner_loop_b(x: int, y: int) -> bool:
        if y >= len(container):
            return inner_loop_a(x + 1)
        return inner_loop_c(x, y, y + 1)

    def inner_loop_a(x: int) -> bool:
        if x >= len(container) - 2:
            return False
        return inner_loop_b(x, x + 1)

    return inner_loop_a(0)