from typing import List

def search(sequence: List[int]) -> int:
    if not sequence:
        return -1  # Handle empty input gracefully

    max_limit: int = max(sequence)
    counts: List[int] = [0] * (max_limit + 1)

    def tally(pos: int) -> None:
        if pos >= len(sequence):
            return
        counts[sequence[pos]] += 1
        tally(pos + 1)

    tally(1)

    result_holder: int = -1
    cursor: int = 1
    while cursor < len(counts):
        if not (counts[cursor] < cursor):
            result_holder = cursor
        cursor += 1
    return result_holder