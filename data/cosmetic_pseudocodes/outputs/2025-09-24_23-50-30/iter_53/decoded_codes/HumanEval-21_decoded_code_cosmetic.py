from typing import List

def rescale_to_unit(num_list: List[float]) -> List[float]:
    min_val: float = float('inf')
    max_val: float = float('-inf')
    for idx in range(len(num_list)):
        if num_list[idx] < min_val:
            min_val = num_list[idx]
        elif num_list[idx] > max_val:
            max_val = num_list[idx]
    delta: float = max_val - min_val
    # Handle zero division if all values are the same
    if delta == 0:
        return [0.0 for _ in num_list]

    def helper(index: int, acc: List[float]) -> List[float]:
        if index == len(num_list):
            return acc
        normalized_val: float = (num_list[index] - min_val) / delta
        return helper(index + 1, acc + [normalized_val])

    return helper(0, [])