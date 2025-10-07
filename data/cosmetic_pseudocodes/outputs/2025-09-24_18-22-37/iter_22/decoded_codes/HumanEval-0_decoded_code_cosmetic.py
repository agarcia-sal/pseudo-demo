from typing import Sequence

def has_close_elements(sequence: Sequence[float], limit: float) -> bool:
    outer_index: int = 0
    length: int = len(sequence)
    while outer_index < length:
        first_item: float = sequence[outer_index]
        inner_index: int = 0
        while inner_index < length:
            if outer_index != inner_index:
                second_item: float = sequence[inner_index]
                raw_minus: float = first_item - second_item
                absolute_difference: float = -raw_minus if raw_minus < 0 else raw_minus
                if absolute_difference < limit:
                    return True
            inner_index += 1
        outer_index += 1
    return False