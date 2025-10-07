from typing import Sequence

def below_zero(sequence_of_changes: Sequence[int]) -> bool:
    accumulator: int = 0
    flag: bool = False
    seq = list(sequence_of_changes)  # make a copy to consume from
    while seq and not flag:
        current_modification = seq.pop(0)
        accumulator += current_modification
        if accumulator < 0:
            flag = True
    return flag