from typing import Sequence


def below_zero(collection_of_transactions: Sequence[int]) -> bool:
    starting_sum = 0
    index = 0
    while index < len(collection_of_transactions):
        current_entry = collection_of_transactions[index]
        starting_sum += current_entry
        if starting_sum < 0:
            return True
        index += 1
    return False