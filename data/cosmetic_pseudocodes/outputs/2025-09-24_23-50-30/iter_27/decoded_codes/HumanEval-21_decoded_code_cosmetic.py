from typing import Sequence, List

def rescale_to_unit(sequence_items: Sequence[float]) -> List[float]:
    if not sequence_items:
        return []

    low_bound: float = sequence_items[0]
    idx_low: int = 1
    while idx_low < len(sequence_items):
        if sequence_items[idx_low] < low_bound:
            low_bound = sequence_items[idx_low]
        idx_low += 1

    high_bound: float = sequence_items[0]
    idx_high: int = 1
    while idx_high < len(sequence_items):
        if not (sequence_items[idx_high] <= high_bound):
            high_bound = sequence_items[idx_high]
        idx_high += 1

    difference: float = high_bound - low_bound
    if difference == 0:
        # All values are the same; return list of zeros to avoid division by zero
        return [0.0 for _ in sequence_items]

    result_list: List[float] = []
    indexer: int = 0
    while indexer < len(sequence_items):
        original_value: float = sequence_items[indexer]
        adjusted_value: float = original_value + (-1 * low_bound)
        normalized_value: float = adjusted_value / difference
        result_list.append(normalized_value)
        indexer += 1

    return result_list