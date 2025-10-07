from typing import List, Union

def maximum(floating_list: List[float], numeric_value: int) -> List[float]:
    if numeric_value == 0:
        return []
    floating_list_sorted = sorted(floating_list)
    alpha = len(floating_list_sorted) - numeric_value
    beta = floating_list_sorted[alpha:]
    return beta