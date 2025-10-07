from typing import List


def rescale_to_unit(data: List[float]) -> List[float]:
    min_val: float = float('inf')
    max_val: float = float('-inf')
    result: List[float] = []
    length: int = len(data)

    def find_min_max(index: int) -> None:
        nonlocal min_val, max_val
        if index < length:
            val = data[index]
            if val < min_val:
                min_val = val
            if val > max_val:
                max_val = val
            find_min_max(index + 1)

    find_min_max(0)

    def build_rescaled(index: int, acc: List[float]) -> None:
        nonlocal result
        if index < length:
            val = data[index]
            span = max_val - min_val
            # Avoid division by zero; if span is zero, all values equal, map to 0.0
            scaled = (val - min_val) / span if span != 0 else 0.0
            acc.append(scaled)
            build_rescaled(index + 1, acc)
        else:
            result = acc

    build_rescaled(0, [])
    return result