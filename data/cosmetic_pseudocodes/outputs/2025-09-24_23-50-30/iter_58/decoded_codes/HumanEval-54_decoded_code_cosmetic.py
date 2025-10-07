from typing import Sequence

def same_chars(parameter_a: Sequence[str], parameter_b: Sequence[str]) -> bool:
    container_x: set[str] = set()
    container_y: set[str] = set()
    index_m: int = 0
    while index_m < len(parameter_a):
        container_x.add(parameter_a[index_m])
        index_m += 1
    index_n: int = 0
    while index_n < len(parameter_b):
        container_y.add(parameter_b[index_n])
        index_n += 1
    return not (container_x.difference(container_y) or container_y.difference(container_x))