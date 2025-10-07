from typing import List


def minSubArraySum(array_of_ints: List[int]) -> int:
    accumulator: int = 0
    peak: int = 0
    iterator_index: int = 0

    length: int = len(array_of_ints)
    while iterator_index < length:
        current_element: int = array_of_ints[iterator_index]
        increment_value: int = -current_element
        accumulator += increment_value

        if accumulator < 0:
            accumulator = 0

        if accumulator > peak:
            peak = accumulator

        iterator_index += 1

    if peak == 0:
        temp_max: int = -array_of_ints[0]
        idx: int = 1
        while idx < length:
            current_neg: int = -array_of_ints[idx]
            if current_neg > temp_max:
                temp_max = current_neg
            idx += 1
        peak = temp_max

    result: int = -peak
    return result