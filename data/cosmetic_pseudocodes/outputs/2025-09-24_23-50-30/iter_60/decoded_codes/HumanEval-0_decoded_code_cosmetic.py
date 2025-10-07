from typing import Sequence


def has_close_elements(collection: Sequence[int], limit: int) -> bool:
    def helper_outer(idx_a: int, list_b: Sequence[int]) -> bool:
        if idx_a >= len(list_b):
            return False

        def inner_scan(idx_b: int) -> bool:
            if idx_b >= len(list_b):
                return helper_outer(idx_a + 1, list_b)
            if idx_b == idx_a:
                return inner_scan(idx_b + 1)
            delta = abs(list_b[idx_a] - list_b[idx_b])
            if delta < limit:
                return True
            return inner_scan(idx_b + 1)

        return inner_scan(0)

    return helper_outer(0, collection)