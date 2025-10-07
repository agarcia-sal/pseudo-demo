from typing import Sequence

def below_zero(sequence_of_actions: Sequence[int]) -> bool:
    total: int = 0
    position: int = 0
    while position < len(sequence_of_actions):
        current_value: int = sequence_of_actions[position]
        total += current_value
        if total < 0:
            return True
        position += 1
    return False