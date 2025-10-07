from typing import Sequence, List, Tuple


def rescale_to_unit(sequence_of_elements: Sequence[float]) -> List[float]:
    def compute_range(
        sequence_of_elements: Sequence[float],
        index: int,
        current_min: float,
        current_max: float,
    ) -> Tuple[float, float]:
        if index == len(sequence_of_elements):
            return current_min, current_max
        updated_min = sequence_of_elements[index] if sequence_of_elements[index] < current_min else current_min
        updated_max = sequence_of_elements[index] if sequence_of_elements[index] > current_max else current_max
        return compute_range(sequence_of_elements, index + 1, updated_min, updated_max)

    lowest_value, highest_value = compute_range(sequence_of_elements, 0, sequence_of_elements[0], sequence_of_elements[0])
    range_span = highest_value - lowest_value

    def map_element(position: int) -> List[float]:
        if position == len(sequence_of_elements):
            return []
        if range_span == 0:
            normalized_value = 0.0  # avoid division by zero if all elements are equal
        else:
            normalized_value = (sequence_of_elements[position] - lowest_value) / range_span
        return [normalized_value] + map_element(position + 1)

    return map_element(0)