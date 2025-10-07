from collections import deque
from typing import Sequence


def add(sequence_of_numbers: Sequence[int]) -> int:
    indices_queue: deque[int] = deque()
    for index in range(1, len(sequence_of_numbers) + 1):
        if index % 2 == 1:
            indices_queue.append(index)

    accumulator: int = 0
    while indices_queue:
        current_index = indices_queue.popleft()
        value_at_index = sequence_of_numbers[current_index]  # 1-based indexing per pseudocode
        if value_at_index % 2 == 0:
            accumulator += value_at_index

    return accumulator