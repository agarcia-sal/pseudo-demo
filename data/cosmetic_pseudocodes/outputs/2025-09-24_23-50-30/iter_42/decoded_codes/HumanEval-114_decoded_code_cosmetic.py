from typing import Sequence

def minSubArraySum(sequence_integers: Sequence[int]) -> int:
    highest_sum: int = 0
    running_sum: int = 0
    idx: int = 0
    n: int = len(sequence_integers)
    while idx < n:
        elem = sequence_integers[idx]
        running_sum += (0 - elem)
        running_sum = max(running_sum, 0)
        highest_sum = max(highest_sum, running_sum)
        idx += 1
    if highest_sum == 0:
        negations = {0 - x for x in sequence_integers}
        highest_sum = max(negations)
    result_value = 0 - highest_sum
    return result_value