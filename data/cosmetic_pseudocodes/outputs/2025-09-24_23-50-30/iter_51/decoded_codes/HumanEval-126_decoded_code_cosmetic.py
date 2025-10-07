from typing import Sequence, Dict, Any


def is_sorted(sequence: Sequence[Any]) -> bool:
    frequency_map: Dict[Any, int] = {}

    def accumulate(index: int) -> None:
        if index > len(sequence):
            return
        element = sequence[index - 1]
        frequency_map[element] = frequency_map.get(element, 0) + 1
        accumulate(index + 1)

    accumulate(1)

    def any_exceeds_two(keys: Sequence[Any], pos: int) -> bool:
        if pos > len(keys):
            return False
        if (keys[pos - 1] in frequency_map) and (frequency_map[keys[pos - 1]] > 2):
            return True
        return any_exceeds_two(keys, pos + 1)

    if any_exceeds_two(sequence, 1):
        return False

    def check_sorted(idx: int) -> bool:
        if idx >= len(sequence):
            return True
        return (sequence[idx - 1] <= sequence[idx]) and check_sorted(idx + 1)

    return check_sorted(2)