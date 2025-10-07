from typing import Sequence


def mean_absolute_deviation(numbers: Sequence[float]) -> float:
    def compute_sum(nums: Sequence[float], idx: int) -> float:
        if idx < 0:
            return 0.0
        return nums[idx] + compute_sum(nums, idx - 1)

    count: int = 0
    for _ in numbers:
        count += 1

    aggregate: float = compute_sum(numbers, count - 1)
    average: float = aggregate / count

    def accumulate_abs_diff(nums: Sequence[float], idx: int, acc: float) -> float:
        if idx >= count:
            return acc
        return accumulate_abs_diff(nums, idx + 1, acc + abs(nums[idx] - average))

    sum_abs_diff: float = accumulate_abs_diff(numbers, 0, 0.0)
    mad: float = sum_abs_diff / count
    return mad