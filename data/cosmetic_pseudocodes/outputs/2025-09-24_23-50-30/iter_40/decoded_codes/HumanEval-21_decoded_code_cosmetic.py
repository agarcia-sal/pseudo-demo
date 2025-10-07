from typing import List


def rescale_to_unit(series: List[float]) -> List[float]:
    if not series:
        return []

    lower_bound: float = series[0]
    upper_bound: float = series[0]

    for element in series:
        if element < lower_bound:
            lower_bound = element
        elif element > upper_bound:
            upper_bound = element

    range_diff: float = upper_bound - lower_bound
    if range_diff == 0:
        # All elements are the same, map all to 0.0 to avoid division by zero
        return [0.0] * len(series)

    result: List[float] = [(item - lower_bound) / range_diff for item in series]

    return result