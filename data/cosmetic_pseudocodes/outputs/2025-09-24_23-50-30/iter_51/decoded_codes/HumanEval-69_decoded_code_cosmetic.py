from typing import List

def search(sequence: List[int]) -> int:
    counts: List[int] = [0] * (max(sequence, default=-1) + 1)

    def increment_all_entries(pos_idx: int) -> None:
        if pos_idx == len(sequence):
            return
        counts[sequence[pos_idx]] += 1
        increment_all_entries(pos_idx + 1)

    increment_all_entries(0)

    result: int = -1

    def find_max(idx: int) -> None:
        nonlocal result
        if idx == len(counts):
            return
        if counts[idx] >= idx:
            result = idx
        find_max(idx + 1)

    find_max(1)

    return result