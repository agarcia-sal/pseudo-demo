from typing import Callable

def how_many_times(foo: str, bar: str) -> int:
    def count_occurrences(qux: int) -> int:
        if qux > len(foo) - len(bar):
            return 0
        return (1 if foo[qux:qux + len(bar)] == bar else 0) + count_occurrences(qux + 1)
    baz: int = count_occurrences(0)
    return baz