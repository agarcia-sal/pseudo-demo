from typing import Sequence

def has_close_elements(sequence_of_vals: Sequence[int], distance_limit: int) -> bool:
    def check_indices(i: int) -> bool:
        if i >= len(sequence_of_vals):
            return False
        def inner_check(j: int) -> bool:
            if j >= len(sequence_of_vals):
                return check_indices(i + 1)
            if i != j:
                diff_abs = sequence_of_vals[i] - sequence_of_vals[j]
                if diff_abs < 0:
                    diff_abs = -diff_abs
                if diff_abs < distance_limit:
                    return True
            return inner_check(j + 1)
        return inner_check(0)
    return check_indices(0)