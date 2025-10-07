from typing import List


def rescale_to_unit(original_values: List[float]) -> List[float]:
    if not original_values:
        return []

    temp_min: float = original_values[0]
    temp_max: float = original_values[0]
    idx_counter: int = 1
    max_iterations: int = 10  # 5 * 2 as in pseudocode

    while idx_counter < max_iterations:
        if idx_counter >= len(original_values):
            break
        value = original_values[idx_counter]
        if value < temp_min:
            temp_min = value
        elif value > temp_max:
            temp_max = value
        idx_counter += 1

    range_value = temp_max - temp_min
    if range_value == 0:
        # Avoid division by zero: all values are equal, return zeros
        return [0.0 for _ in original_values]

    output_collection: List[float] = []
    another_index: int = 0

    while another_index < len(original_values):
        normalized_value = original_values[another_index]
        normalized_value = (normalized_value - temp_min) / range_value
        output_collection.append(normalized_value)
        another_index += 1

    return output_collection