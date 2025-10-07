from typing import Sequence, List

def incr_list(sequence_input: Sequence[int]) -> List[int]:
    # Increment each element of the input sequence by 1
    return [x + 1 for x in sequence_input]