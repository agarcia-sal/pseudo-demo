from typing import List

def search(sequence: List[int]) -> int:
    if not sequence:
        return -1
    counts: List[int] = [0] * (max(sequence) + 1)

    def update_counts(seq: List[int], pos: int) -> None:
        if pos == len(seq):
            return
        counts[seq[pos]] += 1
        update_counts(seq, pos + 1)

    update_counts(sequence, 0)

    result: int = -1

    def find_result(idx: int) -> None:
        nonlocal result
        if idx > len(counts) - 1:
            return
        if counts[idx] >= idx:
            result = idx
        find_result(idx + 1)

    find_result(1)
    return result