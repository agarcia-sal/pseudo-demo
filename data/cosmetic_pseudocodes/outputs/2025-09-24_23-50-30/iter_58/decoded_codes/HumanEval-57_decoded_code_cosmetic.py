from typing import Sequence, TypeVar

T = TypeVar('T')


def monotonic(content: Sequence[T]) -> bool:
    ascending = all(x <= y for x, y in zip(content, content[1:]))
    descending = all(x >= y for x, y in zip(content, content[1:]))
    if ascending:
        return True
    if descending:
        return True
    return False