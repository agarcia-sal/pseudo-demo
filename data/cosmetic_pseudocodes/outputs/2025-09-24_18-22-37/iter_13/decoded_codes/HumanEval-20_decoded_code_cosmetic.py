from typing import Sequence, Optional, Tuple, Union


def find_closest_elements(sequence_of_values: Sequence[Union[int, float]]) -> Optional[Tuple[Union[int, float], Union[int, float]]]:
    result_pair: Optional[Tuple[Union[int, float], Union[int, float]]] = None
    smallest_gap: Optional[Union[int, float]] = None

    for outer_idx in range(len(sequence_of_values)):
        first_val = sequence_of_values[outer_idx]
        for inner_idx in range(len(sequence_of_values)):
            if outer_idx != inner_idx:
                second_val = sequence_of_values[inner_idx]
                if smallest_gap is None:
                    gap = first_val - second_val
                    if gap < 0:
                        gap = -gap
                    smallest_gap = gap
                    if first_val < second_val:
                        result_pair = (first_val, second_val)
                    else:
                        result_pair = (second_val, first_val)
                else:
                    current_gap = first_val - second_val
                    if current_gap < 0:
                        current_gap = -current_gap
                    if current_gap < smallest_gap:
                        smallest_gap = current_gap
                        if first_val < second_val:
                            result_pair = (first_val, second_val)
                        else:
                            result_pair = (second_val, first_val)
    return result_pair