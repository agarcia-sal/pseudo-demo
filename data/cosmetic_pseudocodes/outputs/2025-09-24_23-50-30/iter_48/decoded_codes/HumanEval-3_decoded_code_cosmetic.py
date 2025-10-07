from typing import Sequence


def below_zero(sequence_of_values: Sequence[int]) -> bool:
    accumulator: int = 0
    index_tracker: int = 0
    has_negative_balance: bool = False

    # Iterate until end of sequence or negative balance encountered
    while index_tracker < len(sequence_of_values) and not has_negative_balance:
        accumulator += sequence_of_values[index_tracker]
        has_negative_balance = accumulator < 0
        index_tracker += 1

    return has_negative_balance