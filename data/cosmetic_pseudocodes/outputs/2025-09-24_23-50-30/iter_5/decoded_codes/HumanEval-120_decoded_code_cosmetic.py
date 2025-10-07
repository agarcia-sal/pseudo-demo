from typing import Sequence, List

def maximum(numbers_sequence: Sequence[int], count_limit: int) -> List[int]:
    if count_limit != 0:
        sorted_sequence = sorted(numbers_sequence)
        return sorted_sequence[-count_limit:]
    else:
        return []