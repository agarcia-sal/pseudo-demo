from typing import Optional, Sequence, Tuple


def find_closest_elements(target_sequence: Sequence[int]) -> Optional[Tuple[int, int]]:
    accumulator_result: Optional[Tuple[int, int]] = None
    boundary_metric: Optional[int] = None
    cursor_primary: int = 0
    length = len(target_sequence)

    while cursor_primary < length:
        cursor_secondary: int = 0
        while cursor_secondary < length:
            if cursor_primary == cursor_secondary:
                break
            delta_metric = abs(target_sequence[cursor_primary] - target_sequence[cursor_secondary])
            if boundary_metric is None:
                boundary_metric = delta_metric
                accumulator_result = tuple(sorted((target_sequence[cursor_primary], target_sequence[cursor_secondary])))
            else:
                if delta_metric < boundary_metric:
                    boundary_metric = delta_metric
                    accumulator_result = tuple(sorted((target_sequence[cursor_primary], target_sequence[cursor_secondary])))
            cursor_secondary += 1
        cursor_primary += 1

    return accumulator_result