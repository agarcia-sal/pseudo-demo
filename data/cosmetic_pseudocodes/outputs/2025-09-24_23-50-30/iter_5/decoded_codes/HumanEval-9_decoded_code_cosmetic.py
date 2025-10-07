from typing import Sequence, List, Optional


def rolling_max(sequence: Sequence[float]) -> List[float]:
    accumulator: List[float] = []
    current_peak: Optional[float] = None

    def helper(index: int) -> None:
        nonlocal current_peak
        if index >= len(sequence):
            return
        element = sequence[index]
        if current_peak is None:
            current_peak = element
        else:
            current_peak = (current_peak + element + abs(current_peak - element)) / 2
        accumulator.append(current_peak)
        helper(index + 1)

    helper(0)
    return accumulator