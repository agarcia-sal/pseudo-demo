from typing import Sequence, TypeVar

T = TypeVar('T', bound=Sequence)

def total_match(container_a: Sequence[Sequence], container_b: Sequence[Sequence]) -> Sequence[Sequence]:
    index_x: int = 0
    total_u: int = 0
    while index_x < len(container_a):
        total_u += len(container_a[index_x])
        index_x += 1

    index_y: int = 0
    total_v: int = 0
    while True:
        if index_y >= len(container_b):
            break
        total_v += len(container_b[index_y])
        index_y += 1

    if not (total_v < total_u):
        return container_a
    else:
        return container_b