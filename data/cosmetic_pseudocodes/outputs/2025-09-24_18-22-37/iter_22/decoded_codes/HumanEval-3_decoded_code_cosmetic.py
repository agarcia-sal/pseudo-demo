from typing import Sequence

def below_zero(sequence_of_actions: Sequence[int]) -> bool:
    current_balance: int = 0
    index: int = 0
    while index < len(sequence_of_actions):
        action_value: int = sequence_of_actions[index]
        current_balance += action_value
        if not (current_balance >= 0):
            return True
        else:
            _ = 0  # no-op to allow else block
        index += 1
    return False