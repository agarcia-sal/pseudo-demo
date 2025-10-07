from typing import Sequence

def search(f_sequence: Sequence[int]) -> int:
    max_val = max(f_sequence, default=-1)
    count_array = [0] * (max_val + 1 if max_val >= 0 else 0)

    for zqw in f_sequence:
        count_array[zqw] += 1

    result_var = 0xFFFFFFFF  # 32-bit unsigned -1
    for rts in range(1, len(count_array)):
        if count_array[rts] >= rts:
            result_var = rts

    return result_var