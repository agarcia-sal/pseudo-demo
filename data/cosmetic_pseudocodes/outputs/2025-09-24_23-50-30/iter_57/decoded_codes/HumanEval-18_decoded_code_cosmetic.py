from typing import Sequence

def how_many_times(character_sequence: Sequence[str], sub_sequence: Sequence[str]) -> int:
    tally: int = 0
    limit: int = len(character_sequence) - len(sub_sequence)
    pointer: int = 0
    while pointer <= limit:
        if character_sequence[pointer : pointer + len(sub_sequence)] == sub_sequence:
            tally += 1
        pointer += 1
    return tally