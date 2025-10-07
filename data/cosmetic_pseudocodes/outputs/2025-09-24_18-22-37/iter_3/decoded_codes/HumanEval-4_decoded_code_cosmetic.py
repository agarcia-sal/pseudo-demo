from typing import Sequence

def mean_absolute_deviation(array: Sequence[float]) -> float:
    length = len(array)
    if length == 0:
        raise ValueError("mean_absolute_deviation() arg is an empty sequence")

    count = 0
    sum_elements = 0.0
    while count < length:
        sum_elements += array[count]
        count += 1
    average = sum_elements / length

    index = 0
    accumulator = 0.0
    while True:
        if index >= length:
            break
        diff = array[index] - average
        abs_diff = diff if diff >= 0 else -diff
        accumulator += abs_diff
        index += 1

    mad_result = accumulator / length
    return mad_result