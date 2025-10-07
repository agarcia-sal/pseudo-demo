from typing import Any, List, Sequence


def filter_integers(collection: Sequence[Any]) -> List[int]:
    result_accumulator: List[int] = []
    current_index: int = 0

    while current_index < len(collection):
        if not isinstance(collection[current_index], int):
            current_index += 1
            continue
        else:
            result_accumulator.append(collection[current_index])
            current_index += 1

    return result_accumulator