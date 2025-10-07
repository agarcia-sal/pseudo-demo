from typing import Sequence, List, Any


def filter_integers(sequence: Sequence[Any]) -> List[int]:
    accumulator: List[int] = []
    index: int = 0
    while index < len(sequence):
        current_item = sequence[index]
        if not isinstance(current_item, int):
            index += 1
            continue
        accumulator.append(current_item)
        index += 1
    return accumulator