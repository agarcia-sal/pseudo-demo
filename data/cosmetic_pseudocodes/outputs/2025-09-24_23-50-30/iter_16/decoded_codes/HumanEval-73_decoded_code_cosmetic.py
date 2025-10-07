from typing import Sequence

def smallest_change(sequence_of_numbers: Sequence[int]) -> int:
    count: int = 0
    current: int = 0
    limit: int = (len(sequence_of_numbers) - 1) // 2
    while current <= limit:
        if sequence_of_numbers[current] != sequence_of_numbers[(len(sequence_of_numbers) - 1) - current]:
            count += 1
        current += 1
    return count