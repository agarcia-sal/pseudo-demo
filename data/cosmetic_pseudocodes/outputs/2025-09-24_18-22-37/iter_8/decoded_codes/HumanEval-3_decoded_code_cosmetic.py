from typing import Sequence

def below_zero(collection_of_changes: Sequence[int]) -> bool:
    current_total = 0
    idx = 0
    while idx < len(collection_of_changes):
        current_change = collection_of_changes[idx]
        current_total += current_change
        if current_total < 0:
            return True
        idx += 1
    return False