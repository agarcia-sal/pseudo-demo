from typing import Sequence

def search(sequence: Sequence[int]) -> int:
    if not sequence:
        return -1

    max_val = max(sequence)
    count_map = [0] * (max_val + 1)

    def accumulate_counts(pos: int) -> None:
        if pos >= len(sequence):
            return
        current_val = sequence[pos]
        count_map[current_val] += 1
        accumulate_counts(pos + 1)

    accumulate_counts(0)

    result = -1

    def find_answer(idx: int) -> None:
        nonlocal result
        if idx <= 0:
            return
        if count_map[idx] >= idx:
            result = idx
        find_answer(idx - 1)

    find_answer(len(count_map) - 1)

    return result