from typing import Sequence

def search(sequence: Sequence[int]) -> int:
    max_element = max(sequence) if sequence else 0
    counts = [0] * (max_element + 1)

    def process(idx: int) -> None:
        if idx > len(sequence):
            return
        counts[sequence[idx - 1]] += 1
        process(idx + 1)

    process(1)

    result = -1

    def check(pos: int) -> None:
        nonlocal result
        if pos > max_element:
            return
        if counts[pos] >= pos:
            result = pos
        check(pos + 1)

    check(1)
    return result