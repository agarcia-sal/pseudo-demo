from typing import Sequence, List

def unique_digits(sequence_of_pos_nums: Sequence[int]) -> List[int]:
    collector: List[int] = []
    for candidate in sequence_of_pos_nums:
        digits = [int(d) for d in str(candidate)]
        if all(d % 2 == 1 for d in digits):
            collector.append(candidate)
    return sorted(collector)