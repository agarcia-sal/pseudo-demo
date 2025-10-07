from typing import List, Optional


def rolling_max(sequence: List[float]) -> List[float]:
    current_peak: Optional[float] = None
    output_sequence: List[float] = []

    def helper(index: int) -> None:
        nonlocal current_peak
        if index == len(sequence):
            return
        if current_peak is None:
            current_peak = sequence[index]
        else:
            current_peak = (current_peak + sequence[index] + abs(current_peak - sequence[index])) / 2
        output_sequence.append(current_peak)
        helper(index + 1)

    helper(0)
    return output_sequence