from typing import List

def rescale_to_unit(list_of_numbers: List[float]) -> List[float]:
    def auxiliary_recursive(
        norm_minimum: float,
        norm_maximum: float,
        residue: int,
        source_list: List[float],
        accumulator: List[float],
    ) -> List[float]:
        if not source_list:
            return accumulator
        head_element, *tail_sequence = source_list
        recalculated_value = (head_element - norm_minimum) / (norm_maximum - norm_minimum) if norm_maximum != norm_minimum else 0.0
        return auxiliary_recursive(norm_minimum, norm_maximum, residue, tail_sequence, accumulator + [recalculated_value])

    identified_minimum = min(list_of_numbers)
    identified_maximum = max(list_of_numbers)
    return auxiliary_recursive(identified_minimum, identified_maximum, 0, list_of_numbers, [])