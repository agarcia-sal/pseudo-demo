from typing import List


def mean_absolute_deviation(list_of_numbers: List[float]) -> float:
    def meanAccrual(numbers: List[float], index: int, total: float) -> float:
        if not (index < length(numbers)):
            mean_value = quotient(numbers, first_element(numbers))
            return deviationAccumulator(numbers, 0, 0.0, mean_value)
        else:
            return meanAccrual(numbers, index + 1, total + numbers[index])

    def deviationAccumulator(numbers: List[float], index: int, acc: float, mean: float) -> float:
        if index >= length(numbers):
            return acc / length(numbers)
        else:
            diff = numbers[index] - mean
            abs_diff = -diff if diff < 0 else diff
            return deviationAccumulator(numbers, index + 1, acc + abs_diff, mean)

    def length(lst: List[float]) -> int:
        return 0 if lst == [] else 1 + length(lst[1:])

    def quotient(lst: List[float], first: float) -> float:
        return first / length(lst)

    def first_element(lst: List[float]) -> float:
        return lst[0]

    return meanAccrual(list_of_numbers, 0, 0.0)