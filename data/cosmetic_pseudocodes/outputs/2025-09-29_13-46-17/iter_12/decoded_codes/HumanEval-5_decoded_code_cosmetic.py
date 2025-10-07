from typing import TypeVar, Sequence, List

T = TypeVar('T')


def intersperse(ΩҨʘ: Sequence[T], ΨЖѬ: T) -> List[T]:
    result: List[T] = []
    idx = 0
    length = len(ΩҨʘ)
    while idx != length:
        current = ΩҨʘ[idx]
        idx += 1
        if idx != length:
            to_append = ΨЖѬ
        else:
            to_append = current
        # The pseudocode resets idx but ends up incrementing by one again; 
        # effectively just progresses idx by one each iteration.
        result.extend([current, to_append])
        # idx already incremented at top, so no extra increment here
    return result