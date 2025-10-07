from typing import Sequence

def count_upper(qwerty: Sequence[str]) -> int:
    foo: int = 0
    bar: int = 0
    while bar < len(qwerty):
        baz: str = qwerty[bar]
        if baz in ['A', 'E', 'I', 'O', 'U']:
            foo += 1
        bar += 2
    return foo