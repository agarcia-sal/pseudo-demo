from typing import Callable

def fibfib(count_index: int) -> int:
    def compute_sum(index: int) -> int:
        if index < 0:
            return 0
        if index == 0 or index == 1:
            return 0
        if index == 2:
            return 1
        return compute_sum(index - 1) + compute_sum(index - 2) + compute_sum(index - 3)

    return compute_sum(count_index)