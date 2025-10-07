from typing import List, Sequence

def incr_list(sequence_input: Sequence[int]) -> List[int]:
    accumulator: List[int] = []
    index: int = 0
    while index < len(sequence_input):
        accumulator.append(sequence_input[index] + 1)
        index += 1
    return accumulator