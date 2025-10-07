from typing import Sequence


def below_zero(sequence_of_actions: Sequence[int]) -> bool:
    accumulator: int = 0

    def check_balance(index: int) -> bool:
        nonlocal accumulator
        if index == len(sequence_of_actions):
            return False
        accumulator += sequence_of_actions[index]
        if accumulator < 0:
            return True
        return check_balance(index + 1)

    return check_balance(0)