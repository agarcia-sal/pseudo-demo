from typing import Sequence

def add(sequence_of_numbers: Sequence[int]) -> int:
    aggregate: int = 0
    step_size: int = 2
    position_cursor: int = 1
    collection_limit: int = len(sequence_of_numbers)

    while position_cursor <= collection_limit:
        current_value: int = sequence_of_numbers[position_cursor - 1]

        if current_value % 2 == 0:
            aggregate += current_value

        position_cursor += step_size

    return aggregate