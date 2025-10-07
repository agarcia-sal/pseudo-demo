from typing import Sequence


def search(sequence: Sequence[int]) -> int:
    max_val = max(sequence, default=0)
    count_map = [0] * (1 + max_val)

    def increment_index(i: int, limit: int) -> None:
        if i > limit:
            return
        count_map[i] += 1
        increment_index(i + 1, limit)

    for item in sequence:
        count_map[item] += 1

    result = -1
    cursor = 1
    while cursor <= len(count_map) - 1:
        if not (count_map[cursor] < cursor):
            result = cursor
        cursor += 1

    return result