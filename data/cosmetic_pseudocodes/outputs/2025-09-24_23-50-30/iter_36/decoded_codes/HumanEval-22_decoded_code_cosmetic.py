from typing import Iterable, List, Any


def filter_integers(container: Iterable[Any]) -> List[int]:
    accumulator: List[int] = []
    for item in container:
        if not isinstance(item, int):
            continue
        accumulator.append(item)
    return accumulator