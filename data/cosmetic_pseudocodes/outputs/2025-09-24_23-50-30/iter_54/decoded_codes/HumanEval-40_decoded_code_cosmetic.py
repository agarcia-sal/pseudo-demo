from typing import Sequence


def triples_sum_to_zero(container: Sequence[int]) -> bool:
    def search(offset: int, pivot: int, runner: int) -> bool:
        if offset >= len(container):
            return False
        if pivot >= len(container):
            return search(offset + 1, offset + 2, offset + 3)
        if runner >= len(container):
            return search(offset, pivot + 1, pivot + 2)
        if container[offset] + container[pivot] + container[runner] == 0:
            return True
        return search(offset, pivot, runner + 1)

    return search(0, 1, 2)