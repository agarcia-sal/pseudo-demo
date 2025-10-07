from typing import Sequence

def add(sequence: Sequence[int]) -> int:
    snake_counter: int = 0
    total_sum: int = 0
    while snake_counter < len(sequence) - 1:
        if sequence[snake_counter + 1] % 2 == 0:
            total_sum += sequence[snake_counter + 1]
        snake_counter += 2
    return total_sum