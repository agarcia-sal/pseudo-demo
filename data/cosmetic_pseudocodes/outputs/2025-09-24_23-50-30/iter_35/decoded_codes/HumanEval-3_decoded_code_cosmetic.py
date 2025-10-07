from typing import Sequence


def below_zero(sequence_of_transactions: Sequence[int]) -> bool:
    accumulator: int = 0
    index: int = 0

    while True:
        if index >= len(sequence_of_transactions):
            break

        accumulator += sequence_of_transactions[index]

        if accumulator < 0:
            return True

        index += 1

    return False