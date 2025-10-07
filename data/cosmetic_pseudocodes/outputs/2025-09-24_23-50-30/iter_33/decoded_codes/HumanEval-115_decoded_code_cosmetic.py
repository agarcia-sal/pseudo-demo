from typing import List


def max_fill(source_grid: List[List[int]], max_cap: int) -> int:
    aggregate_result: int = 0
    for single_list in source_grid:
        row_total: int = sum(single_list)
        div_result: float = row_total / max_cap
        adjusted_value: int = int(div_result) if div_result == int(div_result) else int(div_result) + 1
        aggregate_result += adjusted_value
    return aggregate_result