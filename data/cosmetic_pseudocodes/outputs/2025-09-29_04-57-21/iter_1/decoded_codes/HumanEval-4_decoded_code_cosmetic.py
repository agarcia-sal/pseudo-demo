from typing import List

def mean_absolute_deviation(list_of_numbers: List[float]) -> float:
    count: int = len(list_of_numbers)
    if count == 0:
        return 0.0
    average: float = sum(list_of_numbers) / count
    deviations: List[float] = [abs(num - average) for num in list_of_numbers]
    mad_result: float = sum(deviations) / count
    return mad_result