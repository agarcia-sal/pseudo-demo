from typing import Sequence

def minSubArraySum(sequence_of_numbers: Sequence[int | float]) -> int | float:
    accumulator: int | float = 0
    best_accumulator: int | float = 0
    cursor: int = 0
    length: int = len(sequence_of_numbers)

    while cursor < length:
        accumulator += -sequence_of_numbers[cursor]
        if accumulator < 0:
            accumulator = 0
        best_accumulator = max(best_accumulator, accumulator)
        cursor += 1

    if best_accumulator == 0:
        score_list: list[int | float] = [-x for x in sequence_of_numbers]
        maximum_value = score_list[0]
        element_ptr = 1
        while element_ptr < len(score_list):
            if maximum_value < score_list[element_ptr]:
                maximum_value = score_list[element_ptr]
            element_ptr += 1
        best_accumulator = maximum_value

    return -best_accumulator