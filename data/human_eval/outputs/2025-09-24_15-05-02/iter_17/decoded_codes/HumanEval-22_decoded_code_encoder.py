from typing import Iterable, List, Union

def filter_integers(values: Iterable[object]) -> List[int]:
    result: List[int] = []
    for x in values:
        if isinstance(x, int):
            result.append(x)
    return result