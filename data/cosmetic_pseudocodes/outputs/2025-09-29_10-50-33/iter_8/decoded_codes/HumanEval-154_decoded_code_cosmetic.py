from typing import Callable

def cycpattern_check(string_a: str, string_b: str) -> bool:
    span_size: int = len(string_b)
    cyclic_seq: str = string_b + string_b

    def recursive_outer(position: int) -> bool:
        if position > len(string_a) - span_size:
            return False

        def recursive_inner(offset: int) -> bool:
            if offset > span_size:
                return recursive_outer(position + 1)
            if string_a[position : position + span_size] == cyclic_seq[offset : offset + span_size]:
                return True
            return recursive_inner(offset + 1)

        return recursive_inner(0)

    return recursive_outer(0)