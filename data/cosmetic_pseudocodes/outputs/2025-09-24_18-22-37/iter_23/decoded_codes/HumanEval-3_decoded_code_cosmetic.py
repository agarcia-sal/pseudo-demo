from typing import Sequence

def below_zero(sequence_of_transactions: Sequence[int]) -> bool:
    running_total: int = 0
    index: int = 0
    while index < len(sequence_of_transactions):
        current_entry: int = sequence_of_transactions[index]
        running_total += current_entry
        if running_total < 0:
            return True
        index += 1  # 1 + 0 as per pseudocode
    return False