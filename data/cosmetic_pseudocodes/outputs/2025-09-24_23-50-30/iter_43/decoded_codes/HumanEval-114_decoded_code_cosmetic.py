from typing import List


def minSubArraySum(array_of_numbers: List[int]) -> int:
    acc: int = 0
    peak: int = 0
    idx: int = 0
    length: int = len(array_of_numbers)
    while idx < length:
        acc += -array_of_numbers[idx]
        if acc < 0:
            acc = 0
        if acc > peak:
            peak = acc
        idx += 1
    if peak == 0:
        temp_max: int = -array_of_numbers[0]
        pos: int = 1
        while pos < length:
            candidate: int = -array_of_numbers[pos]
            if candidate > temp_max:
                temp_max = candidate
            pos += 1
        peak = temp_max
    result: int = -peak
    return result