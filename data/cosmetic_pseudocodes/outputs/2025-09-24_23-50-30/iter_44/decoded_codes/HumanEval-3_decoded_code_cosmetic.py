from typing import Sequence

def below_zero(actions_sequence: Sequence[int]) -> bool:
    def check(index: int, current_sum: int) -> bool:
        if index >= len(actions_sequence):
            return False
        updated_sum = current_sum + actions_sequence[index]
        if updated_sum < 0:
            return True
        return check(index + 1, updated_sum)

    return check(0, 0)