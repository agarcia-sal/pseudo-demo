from typing import Iterable, Union

def minSubArraySum(input_sequence: Iterable[Union[int, float]]) -> Union[int, float]:
    temp_aggregate: Union[int, float] = 0
    peak_aggregate: Union[int, float] = 0

    for element in input_sequence:
        temp_aggregate += 0 - element
        if temp_aggregate < 0:
            temp_aggregate = 0
        if peak_aggregate < temp_aggregate:
            peak_aggregate = temp_aggregate

    if peak_aggregate == 0:
        # max of (0 - x) for x in input_sequence: max(-x) == -min(x)
        max_neg = max(0 - x for x in input_sequence)
        peak_aggregate = max_neg

    answer = 0 - peak_aggregate
    return answer