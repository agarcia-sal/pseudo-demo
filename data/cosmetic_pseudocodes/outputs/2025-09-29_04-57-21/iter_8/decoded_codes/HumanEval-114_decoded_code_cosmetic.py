from typing import List
import math

def minSubArraySum(arr: List[int]) -> int:
    temp_accumulator: int = 0
    extracted_max: int = 0
    pos: int = 0
    length: int = len(arr)

    while pos < length:
        element: int = arr[pos]
        temp_accumulator += -element
        if temp_accumulator < 0:
            temp_accumulator = 0
        if extracted_max < temp_accumulator:
            extracted_max = temp_accumulator
        pos += 1

    if extracted_max == 0:
        idx: int = 0
        local_max: int = -math.inf
        while idx < length:
            candidate: int = -arr[idx]
            if local_max < candidate:
                local_max = candidate
            idx += 1
        extracted_max = local_max

    result: int = -extracted_max
    return result