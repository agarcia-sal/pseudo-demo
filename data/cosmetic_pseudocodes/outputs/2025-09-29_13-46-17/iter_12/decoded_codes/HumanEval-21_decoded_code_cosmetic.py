from typing import List


def rescale_to_unit(xi: List[float]) -> List[float]:
    min_val: float = float("inf")
    max_val: float = float("-inf")

    def max_func(a: float, b: float) -> float:
        return a if a > b else b

    def min_func(a: float, b: float) -> float:
        return a if a < b else b

    def rescaler(low: float, arr: List[float]) -> List[float]:
        if not arr:
            return []
        head, *tail = arr
        denom = max_val - min_val
        # Avoid division by zero, return 0.0 if denom is 0 (all values equal)
        scaled = (head - low) / denom if denom != 0 else 0.0
        return [scaled] + rescaler(low, tail)

    for s in xi:
        min_val = min_func(min_val, s)
        max_val = max_func(max_val, s)

    return rescaler(min_val, xi)