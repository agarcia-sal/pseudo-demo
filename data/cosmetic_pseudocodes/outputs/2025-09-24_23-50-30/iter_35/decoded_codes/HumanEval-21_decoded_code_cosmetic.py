from typing import List, Optional

def rescale_to_unit(sequence_of_values: List[float]) -> List[float]:
    min_val: Optional[float] = None
    max_val: Optional[float] = None
    for val in sequence_of_values:
        if min_val is None or val < min_val:
            min_val = val
        if max_val is None or val > max_val:
            max_val = val
    # Handle edge case where all values are equal or sequence is empty
    denominator = max_val - min_val if (min_val is not None and max_val is not None) else None
    if denominator in (0, None):
        return [0.0 for _ in sequence_of_values]

    def transform_value(index: int, output_accumulator: List[float]) -> List[float]:
        if index >= len(sequence_of_values):
            return output_accumulator
        adjusted = (sequence_of_values[index] - min_val) / denominator  # type: ignore
        output_accumulator.append(adjusted)
        return transform_value(index + 1, output_accumulator)

    return transform_value(0, [])