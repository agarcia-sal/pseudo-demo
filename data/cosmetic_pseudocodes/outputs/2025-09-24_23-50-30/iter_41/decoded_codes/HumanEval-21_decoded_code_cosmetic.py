from typing import Sequence, List, Tuple


def rescale_to_unit(input_sequence: Sequence[float]) -> List[float]:
    def compute_min_max(seq: Sequence[float], low: float, high: float, idx: int) -> Tuple[float, float]:
        if idx == len(seq):
            return (low, high)
        current_val = seq[idx]
        updated_low = low if low < current_val else current_val
        updated_high = high if high > current_val else current_val
        return compute_min_max(seq, updated_low, updated_high, idx + 1)

    min_val, max_val = compute_min_max(input_sequence, input_sequence[0], input_sequence[0], 1)

    def normalize_element(value: float, minimum: float, maximum: float) -> float:
        # Handle zero division if all elements are equal
        if maximum == minimum:
            return 0.0
        return (value - minimum) / (maximum - minimum)

    index = 0
    scaled_list: List[float] = []
    while index < len(input_sequence):
        scaled_list.append(normalize_element(input_sequence[index], min_val, max_val))
        index += 1
    return scaled_list