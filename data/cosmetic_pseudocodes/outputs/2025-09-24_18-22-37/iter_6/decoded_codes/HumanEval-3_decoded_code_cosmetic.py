from typing import Sequence

def below_zero(collection_of_actions: Sequence[int]) -> bool:
    running_total: int = 0
    index: int = 0  # zero-based indexing for Python sequences
    while index < len(collection_of_actions):
        current_action: int = collection_of_actions[index]
        running_total += current_action
        if running_total < 0:
            return True
        else:
            index += 1
    return False