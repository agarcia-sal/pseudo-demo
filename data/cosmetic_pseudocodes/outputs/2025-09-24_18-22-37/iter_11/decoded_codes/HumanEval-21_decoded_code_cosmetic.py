from typing import Sequence, List

def rescale_to_unit(number_sequence: Sequence[float]) -> List[float]:
    if not number_sequence:
        return []
    smallest_value: float = number_sequence[0]
    iterator_index: int = 1
    while iterator_index < len(number_sequence):
        if number_sequence[iterator_index] < smallest_value:
            smallest_value = number_sequence[iterator_index]
        iterator_index += 1

    largest_value: float = number_sequence[0]
    index_counter: int = 1
    while index_counter < len(number_sequence):
        if largest_value < number_sequence[index_counter]:
            largest_value = number_sequence[index_counter]
        index_counter += 1

    delta_value = largest_value - smallest_value
    normalized_list: List[float] = []
    element_index: int = 0
    while element_index < len(number_sequence):
        shifted_value = number_sequence[element_index] - smallest_value
        # Avoid division by zero when all values are identical
        normalized_value = shifted_value / delta_value if delta_value != 0 else 0.0
        normalized_list.append(normalized_value)
        element_index += 1

    return normalized_list