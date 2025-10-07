from typing import Sequence


def smallest_change(seq_of_ints: Sequence[int]) -> int:
    def count_diff(i: int, acc: int) -> int:
        if i > (len(seq_of_ints) / 2) - 1:
            return acc
        return count_diff(
            i + 1,
            acc + (1 if seq_of_ints[i] != seq_of_ints[len(seq_of_ints) - i - 1] else 0),
        )

    return count_diff(0, 0)