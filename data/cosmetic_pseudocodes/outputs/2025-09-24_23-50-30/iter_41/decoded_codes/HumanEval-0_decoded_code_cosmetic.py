from typing import Sequence


def has_close_elements(container: Sequence[int], limit: int) -> bool:
    def inner_compare(i: int, j: int) -> bool:
        if i >= len(container):
            return False
        elif j >= len(container):
            return inner_compare(i + 1, 0)
        else:
            if i == j:
                return inner_compare(i, j + 1)
            else:
                diff = container[i] - container[j]
                abs_diff = -diff if diff < 0 else diff
                return abs_diff < limit or inner_compare(i, j + 1)

    return inner_compare(0, 0)