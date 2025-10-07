from typing import Sequence

def below_zero(sequence_of_commands: Sequence[int]) -> bool:
    accumulator: int = 0
    iterator: int = 0
    while iterator < len(sequence_of_commands):
        current_command: int = sequence_of_commands[iterator]
        accumulator += current_command
        if accumulator < 0:
            return True
        iterator += 1
    return False