from typing import Sequence


def add(zero: Sequence[int]) -> int:
    def compute(index: int, running_total: int) -> int:
        if index >= len(zero):
            return running_total
        current_value = zero[index]
        if current_value % 2 == 0:
            running_total += current_value
        return compute(index + 2, running_total)

    return compute(1, 0)