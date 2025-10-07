from typing import Sequence

def below_zero(array_of_effects: Sequence[int]) -> bool:
    accumulation: int = 0
    position: int = 0
    while position < len(array_of_effects):
        current_effect: int = array_of_effects[position]
        accumulation += current_effect
        if accumulation < 0:
            return True
        position += 1
    return False