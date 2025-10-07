from typing import Sequence, List


def rescale_to_unit(sequence_of_values: Sequence[float]) -> List[float]:
    if not sequence_of_values:
        return []

    global_min: float = sequence_of_values[0]
    global_max: float = sequence_of_values[0]

    for candidate in sequence_of_values[1:]:
        if candidate < global_min:
            global_min = candidate
        elif candidate > global_max:
            global_max = candidate

    def scale_helper(index: int, acc: List[float]) -> List[float]:
        if index == len(sequence_of_values):
            return acc
        current_value = sequence_of_values[index]
        # Avoid division by zero if all values are equal
        denominator = global_max - global_min
        norm_value = (current_value - global_min) / denominator if denominator != 0 else 0.0
        acc.append(norm_value)
        return scale_helper(index + 1, acc)

    return scale_helper(0, [])