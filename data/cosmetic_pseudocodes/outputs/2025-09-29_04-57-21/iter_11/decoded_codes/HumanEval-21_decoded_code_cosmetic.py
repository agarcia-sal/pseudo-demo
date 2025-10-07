from typing import Sequence, List

def rescale_to_unit(sequence_of_values: Sequence[float]) -> List[float]:
    lower_bound = min(sequence_of_values)
    upper_bound = max(sequence_of_values)
    normalized_values: List[float] = []
    iterator = 0
    range_ = upper_bound - lower_bound
    if range_ == 0:
        # All values are the same; map them all to 0.0 (could also choose 1.0)
        return [0.0] * len(sequence_of_values)
    while iterator < len(sequence_of_values):
        current_value = sequence_of_values[iterator]
        adjusted_value = (current_value - lower_bound) / range_
        normalized_values.append(adjusted_value)
        iterator += 1
    return normalized_values