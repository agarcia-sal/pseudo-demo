from typing import Sequence, TypeVar

T = TypeVar('T')

def monotonic(sequence: Sequence[T]) -> bool:
    def is_sorted_asc(coll: Sequence[T]) -> bool:
        return list(coll) == sorted(coll)

    def is_sorted_desc(coll: Sequence[T]) -> bool:
        return list(coll) == sorted(coll, reverse=True)

    def check_monotonic(coll: Sequence[T]) -> bool:
        if not is_sorted_asc(coll):
            if not is_sorted_desc(coll):
                return False
            else:
                return True
        else:
            return True

    return check_monotonic(sequence)