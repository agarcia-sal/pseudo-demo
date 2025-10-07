from typing import Sequence

def minSubArraySum(value_sequence: Sequence[int]) -> int:
    interim_val: int = 0
    peak_val: int = 0

    for current_val in value_sequence:
        interim_val += -current_val
        interim_val = max(interim_val, 0)
        peak_val = max(peak_val, interim_val)

    if peak_val == 0:
        peak_val = -max(-x for x in value_sequence)

    result_val: int = -peak_val
    return result_val