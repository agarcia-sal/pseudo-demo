from typing import Sequence

def has_close_elements(sequence_collection: Sequence[float], limit_param: float) -> bool:
    outer_pos: int = 0
    while outer_pos < len(sequence_collection):
        inner_pos: int = 0
        while inner_pos < len(sequence_collection):
            if outer_pos != inner_pos:
                delta_var: float = abs(sequence_collection[outer_pos] - sequence_collection[inner_pos])
                if delta_var < limit_param:
                    return True
            inner_pos += 1
        outer_pos += 1
    return False