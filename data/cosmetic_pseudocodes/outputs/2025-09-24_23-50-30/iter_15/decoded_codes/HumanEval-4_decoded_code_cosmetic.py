from collections import deque
from typing import List

def mean_absolute_deviation(original_array: List[float]) -> float:
    count: int = len(original_array)
    aggregate_sum: float = 0.0
    for index in range(count):
        aggregate_sum += original_array[index]

    average: float = aggregate_sum / count

    deviations_queue: deque[float] = deque()
    for each_element in original_array:
        deviations_queue.append(each_element - average if each_element >= average else average - each_element)

    accumulated_deviation: float = 0.0
    while len(deviations_queue) > 0:
        accumulated_deviation += deviations_queue.popleft()

    result: float = accumulated_deviation / count

    return result