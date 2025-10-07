from typing import Sequence, TypeVar

T = TypeVar('T')

def strlen(string: Sequence[T]) -> int:
    def recurse(s: Sequence[T]) -> int:
        if s:
            return 1 + recurse(s[1:])
        else:
            return 0
    return recurse(string)