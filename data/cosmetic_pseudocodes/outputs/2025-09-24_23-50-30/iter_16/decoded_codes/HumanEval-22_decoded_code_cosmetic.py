from typing import Iterable, List, Union

def filter_integers(sequence: Iterable[object]) -> List[int]:
    accumulation: List[int] = []
    for candidate in sequence:
        if not isinstance(candidate, int):
            continue
        accumulation.append(candidate)
    return accumulation