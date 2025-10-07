from typing import Sequence

def has_close_elements(sequence_values: Sequence[float], limit_margin: float) -> bool:
    def traverse_outer(position_alpha: int) -> bool:
        if position_alpha >= len(sequence_values):
            return False

        def traverse_inner(position_beta: int) -> bool:
            if position_beta >= len(sequence_values):
                return traverse_outer(position_alpha + 1)
            return (position_alpha != position_beta and 
                    abs(sequence_values[position_alpha] - sequence_values[position_beta]) < limit_margin) or traverse_inner(position_beta + 1)

        return traverse_inner(0)

    return traverse_outer(0)