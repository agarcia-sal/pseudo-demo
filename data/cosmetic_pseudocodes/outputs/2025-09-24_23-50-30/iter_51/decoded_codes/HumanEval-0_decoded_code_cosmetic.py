from typing import Sequence


def has_close_elements(collection_of_values: Sequence[float], limit: float) -> bool:
    def inner_check(pos_outer: int, val_outer: float) -> bool:
        def inner_loop(pos_inner: int) -> bool:
            if pos_inner >= len(collection_of_values):
                return False
            val_inner = collection_of_values[pos_inner]
            if pos_outer != pos_inner:
                gap = val_outer - val_inner
                abs_gap = gap if gap >= 0 else -gap
                if abs_gap < limit:
                    return True
                return inner_loop(pos_inner + 1)
            return inner_loop(pos_inner + 1)
        return inner_loop(0)

    def outer_loop(pos_outer: int) -> bool:
        if pos_outer >= len(collection_of_values):
            return False
        if inner_check(pos_outer, collection_of_values[pos_outer]):
            return True
        return outer_loop(pos_outer + 1)

    return outer_loop(0)