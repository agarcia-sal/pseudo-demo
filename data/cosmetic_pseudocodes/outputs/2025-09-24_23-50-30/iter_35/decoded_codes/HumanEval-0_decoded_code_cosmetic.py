from typing import Sequence


def has_close_elements(array_of_values: Sequence[float], limit_val: float) -> bool:
    total_elements: int = len(array_of_values)
    pos_primary: int = 0
    while pos_primary < total_elements:
        pos_secondary: int = 0
        while pos_secondary < total_elements:
            if pos_primary != pos_secondary:
                diff_measure: float = array_of_values[pos_primary] - array_of_values[pos_secondary]
                if diff_measure < 0:
                    diff_measure = -diff_measure
                if diff_measure < limit_val:
                    return True
            pos_secondary += 1
        pos_primary += 1
    return False