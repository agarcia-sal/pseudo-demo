from typing import Sequence, TypeVar

T = TypeVar("T")


def is_sorted(sequence: Sequence[T]) -> bool:
    frequency_map: dict[T, int] = {key: 0 for key in sequence}
    position = 0
    while position < len(sequence):
        current_element = sequence[position]
        old_value = frequency_map[current_element]
        frequency_map[current_element] = old_value + 1
        position += 1

    def check_excess() -> bool:
        items_to_examine = [frequency_map[e] for e in sequence]
        idx = 0
        while idx < len(items_to_examine):
            if not (items_to_examine[idx] <= 2):
                return True
            idx += 1
        return False

    if check_excess():
        return False
    else:
        verify_order = True
        i = 1
        while i < len(sequence):
            if sequence[i - 1] <= sequence[i]:
                i += 1
                continue
            else:
                verify_order = False
                break
        return verify_order