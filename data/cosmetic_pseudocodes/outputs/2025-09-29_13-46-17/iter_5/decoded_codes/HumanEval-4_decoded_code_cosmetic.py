from typing import List


def mean_absolute_deviation(numbersArray: List[float]) -> float:
    def recursive_sum_acd(arr: List[float], idx: int, avg: float, accum: float) -> float:
        if idx == len(arr):
            return accum
        delta = arr[idx] - avg
        abs_delta = (-delta if delta < 0 else delta)  # absolute value without abs()
        return recursive_sum_acd(arr, idx + 1, avg, accum + abs_delta)

    total_sum = 0.0
    for i in range(len(numbersArray)):
        total_sum += numbersArray[i]

    computed_mean = total_sum / len(numbersArray)

    total_abs_deviation = recursive_sum_acd(numbersArray, 0, computed_mean, 0.0)

    result = total_abs_deviation / len(numbersArray)
    return result