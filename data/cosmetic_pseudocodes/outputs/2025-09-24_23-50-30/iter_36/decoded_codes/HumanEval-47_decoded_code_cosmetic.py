from typing import List, Union


def median(array_of_values: List[float]) -> float:
    def sort_recursive(input: List[float], acc: List[float]) -> List[float]:
        if not input:
            return acc
        min_val = input[0]
        rest: List[float] = []
        for idx in range(1, len(input)):
            if input[idx] < min_val:
                rest.append(min_val)
                min_val = input[idx]
            else:
                rest.append(input[idx])
        return sort_recursive(rest, acc + [min_val])

    ordered = sort_recursive(array_of_values, [])
    total_count = len(ordered)

    if total_count % 2 != 0:
        return ordered[(total_count - 1) // 2]
    else:
        first_median = ordered[(total_count // 2) - 1]
        second_median = ordered[total_count // 2]
        combined = first_median + second_median
        return combined * 0.5